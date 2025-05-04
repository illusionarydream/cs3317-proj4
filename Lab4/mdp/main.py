import argparse
from mdp import NumberLineMDP, BlackjackMDP
from mdp_algorithm import ValueIteration, PolicyIteration


def create_mdp(mdp_type, **kwargs):
    """Create an MDP instance based on the type."""
    if mdp_type == "numberline":
        return NumberLineMDP(n=kwargs.get("n", 5))
    elif mdp_type == "blackjack":
        return BlackjackMDP(
            cardValues=kwargs.get("card_values", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            multiplicity=kwargs.get("multiplicity", 4),
            threshold=kwargs.get("threshold", 21),
            peekCost=kwargs.get("peek_cost", 1),
        )
    else:
        raise ValueError(f"Unknown MDP type: {mdp_type}")


def solve_mdp(mdp, algorithm_type):
    """Solve the MDP using the specified algorithm."""
    if algorithm_type in ["value_iteration", "policy_iteration"]:
        # MDP-based algorithms
        algorithm = ValueIteration() if algorithm_type == "value_iteration" else PolicyIteration()
        algorithm.solve(mdp)
        return algorithm.V, algorithm.pi
    else:
        raise ValueError(f"Unknown algorithm type: {algorithm_type}")


def main():
    parser = argparse.ArgumentParser(description="Solve MDPs using different algorithms")

    # MDP selection
    parser.add_argument("--mdp", choices=["numberline", "blackjack"], required=True, help="Type of MDP to solve")

    # MDP parameters
    parser.add_argument("--n", type=int, default=5, help="Size parameter for NumberLineMDP")
    parser.add_argument("--card-values", type=int, nargs="+", default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], help="Card values for BlackjackMDP")
    parser.add_argument("--multiplicity", type=int, default=4, help="Card multiplicity for BlackjackMDP")
    parser.add_argument("--threshold", type=int, default=21, help="Threshold for BlackjackMDP")
    parser.add_argument("--peek-cost", type=int, default=1, help="Peek cost for BlackjackMDP")

    # Algorithm selection
    parser.add_argument("--algorithm", choices=["value_iteration", "policy_iteration"], required=True, help="Algorithm to use")

    args = parser.parse_args()

    # Create MDP
    mdp_kwargs = {
        "n": args.n,
        "card_values": args.card_values,
        "multiplicity": args.multiplicity,
        "threshold": args.threshold,
        "peek_cost": args.peek_cost,
    }
    mdp = create_mdp(args.mdp, **mdp_kwargs)

    # Solve MDP
    result = solve_mdp(mdp, args.algorithm)

    # Print results
    def print_summary(title, values, actions=None, max_states=3):
        print(f"\n{title}:")
        # Filter out None values and handle both tuple and non-tuple states
        states = [s for s in values.keys() if s is not None]
        # For BlackjackMDP, sort by total value or number value
        if states and isinstance(states[0], tuple):
            # For BlackjackMDP states: (player_cards, dealer_showing)
            states.sort(key=lambda x: (sum(x[0]), x[1]) if isinstance(x[0], tuple) else x[0])
        else:
            states.sort()
        # Print first few and last few states
        for state in states[:max_states]:
            value_str = f", Value: {values[state]:.2f}"
            action_str = f", Action: {actions[state]}" if actions else ""
            print(f"State: {state}{value_str}{action_str}")
        if len(states) > max_states * 2:
            print("...")
            for state in states[-max_states:]:
                value_str = f", Value: {values[state]:.2f}"
                action_str = f", Action: {actions[state]}" if actions else ""
                print(f"State: {state}{value_str}{action_str}")

    if args.algorithm in ["value_iteration", "policy_iteration"]:
        V, pi = result
        print(f"\n{args.algorithm.title()}: Solution Summary")
        print("-" * 50)
        if args.algorithm == "policy_iteration" and hasattr(result[0], "steps"):
            print("Policy Evaluation/Improvement Steps:")
            for step in result[0].steps:
                print(f"Iteration {step['iteration']}:")
                print(f"  Policy evaluation iterations: {step['eval_iters']}")
                print(f"  Max value change: {step['max_value_change']:.6f}")
                print(f"  Policy changes: {step['policy_changes']}")
        if hasattr(result[0], "numIters"):
            print(f"Final number of iterations: {result[0].numIters}")
        print("\nVerification - Showing all states:")
        # Filter out None states and sort
        states = [s for s in V.keys() if s is not None]
        # Sort based on state type - handle both NumberLine and Blackjack states
        if states and isinstance(states[0], tuple):
            # For Blackjack states: sort by total, then peeked card, then remaining cards
            states.sort(key=lambda x: (x[0] if x[0] is not None else -1, x[1] if x[1] is not None else -1, sum(x[2]) if x[2] is not None else -1))
            # Print summary for Blackjack
            print("\nKey Decision Points:")
            print("-" * 50)
            print("Starting States (Total = 0):")
            start_states = [s for s in states if s[0] == 0][:5]
            for state in start_states:
                print(f"State: {str(state):20} | Value: {V[state]:.2f}    | Action: {pi[state] if state in pi else None}")

            print("\nNear Threshold States (Total = 19-21):")
            threshold_states = [s for s in states if s[0] in [19, 20, 21]][:5]
            for state in threshold_states:
                print(f"State: {str(state):20} | Value: {V[state]:.2f}    | Action: {pi[state] if state in pi else None}")

            print("\nPeeking Decision States (with different peeked cards):")
            peek_states = [s for s in states if s[1] is not None and s[0] in [15, 16, 17]][:5]
            for state in peek_states:
                print(f"State: {str(state):20} | Value: {V[state]:.2f}    | Action: {pi[state] if state in pi else None}")
        else:
            # For NumberLine states: simple numeric sort
            states.sort()
            for state in states:
                action = pi[state] if state in pi else None
                print(f"State: {str(state):20} | Value: {V[state]:.2f}    | Action: {action}")


if __name__ == "__main__":
    main()
