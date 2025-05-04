import collections, random
from typing import List, Tuple, Dict, Any
from mdp import MDP


# An algorithm that solves an MDP (i.e., computes the optimal
# policy).
class MDPAlgorithm:
    """Base class for MDP solving algorithms."""

    def __init__(self):
        self.V = None  # Values for all states
        self.pi = None  # Policy for all states
        self.numIters = 0
        self.steps = []  # Track evaluation/improvement steps

    def computeQ(self, mdp: MDP, V: Dict[Tuple, float], state: Tuple, action: Any) -> float:
        q_value = 0.0
        for next_state, prob, reward in mdp.succAndProbReward(state, action):
            q_value += prob * (reward + mdp.discount() * V[next_state])
        return q_value

    def computeOptimalPolicy(self, mdp: MDP, V: Dict[Tuple, float]) -> Dict[Tuple, Any]:
        """Return the optimal policy given the values V."""
        # BEGIN_YOUR_CODE
        pi = {}
        for state in mdp.states:
            actions = mdp.actions(state)
            if not actions:
                pi[state] = None
                continue
            pi[state] = max(actions, key=lambda a: self.computeQ(mdp, V, state, a))
        return pi
        # END_YOUR_CODE

    def solve(self, mdp: MDP):
        raise NotImplementedError("Override me")


############################################################
class ValueIteration(MDPAlgorithm):
    """Solve the MDP using value iteration.  Your solve() method must set
    - self.V to the dictionary mapping states to optimal values
    - self.pi to the dictionary mapping states to an optimal action
    Note: epsilon is the error tolerance: you should stop value iteration when
    all of the values change by less than epsilon.
    The ValueIteration class is a subclass of MDPAlgorithm.
    """

    def solve(self, mdp: MDP, epsilon=0.001):
        # Initialize
        mdp.computeStates()
        self.V = {state: 0 for state in mdp.states}
        self.numIters = 0
        # BEGIN_YOUR_CODE
        while True:
            delta = 0
            new_V = {}
            for state in mdp.states:
                actions = mdp.actions(state)
                if not actions:
                    new_V[state] = 0
                    continue
                max_q = max(self.computeQ(mdp, self.V, state, action) for action in actions)
                new_V[state] = max_q
                delta = max(delta, abs(new_V[state] - self.V[state]))
            self.V = new_V
            self.numIters += 1
            if delta < epsilon:
                break
        # END_YOUR_CODE

        # Compute optimal policy
        self.pi = self.computeOptimalPolicy(mdp, self.V)
        print(f"ValueIteration: {self.numIters} iterations")


class PolicyIteration(MDPAlgorithm):
    """Policy iteration algorithm."""

    def solve(self, mdp: MDP, epsilon=1e-10):
        """Solve the MDP using policy iteration."""
        # Initialize
        mdp.computeStates()
        self.V = {state: 0 for state in mdp.states}
        self.pi = {state: mdp.actions(state)[0] if mdp.actions(state) else None for state in mdp.states}
        self.numIters = 0

        # BEGIN_YOUR_CODE
        is_policy_stable = False
        while not is_policy_stable:
            # Policy Evaluation
            while True:
                delta = 0
                for state in mdp.states:
                    action = self.pi[state]
                    if action is None:
                        continue
                    new_v = self.computeQ(mdp, self.V, state, action)
                    delta = max(delta, abs(self.V[state] - new_v))
                    self.V[state] = new_v
                if delta < epsilon:
                    break

            # Policy Improvement
            is_policy_stable = True
            for state in mdp.states:
                actions = mdp.actions(state)
                if not actions:
                    continue
                best_action = max(actions, key=lambda a: self.computeQ(mdp, self.V, state, a))
                if best_action != self.pi[state]:
                    self.pi[state] = best_action
                    is_policy_stable = False
            self.numIters += 1
        # END_YOUR_CODE

        print(f"PolicyIteration: {self.numIters} iterations")
