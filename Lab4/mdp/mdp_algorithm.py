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
        """Return Q(state, action) based on V(state)."""
        # BEGIN_YOUR_CODE

        

        # END_YOUR_CODE 
      
    def computeOptimalPolicy(self, mdp: MDP, V: Dict[Tuple, float]) -> Dict[Tuple, Any]:
        """Return the optimal policy given the values V."""
        # BEGIN_YOUR_CODE

        

        # END_YOUR_CODE 
    
    def solve(self, mdp: MDP): 
        raise NotImplementedError("Override me")

############################################################
class ValueIteration(MDPAlgorithm):
    '''Solve the MDP using value iteration.  Your solve() method must set
    - self.V to the dictionary mapping states to optimal values
    - self.pi to the dictionary mapping states to an optimal action
    Note: epsilon is the error tolerance: you should stop value iteration when
    all of the values change by less than epsilon.
    The ValueIteration class is a subclass of MDPAlgorithm.
    '''
    def solve(self, mdp: MDP, epsilon=0.001):
        # Initialize
        mdp.computeStates()
        self.V = {state: 0 for state in mdp.states}
        self.numIters = 0
        # BEGIN_YOUR_CODE
        


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
        self.pi = {state: mdp.actions(state)[0] if mdp.actions(state) else None 
                   for state in mdp.states}
        self.numIters = 0
        
        # BEGIN_YOUR_CODE
          


        # END_YOUR_CODE
        
        print(f"PolicyIteration: {self.numIters} iterations")