"""Class for defining the Belief Base"""
from sympy.logic.boolalg import to_cnf
from typing import List
from .agent import Agent, Action

class BeliefBase:
    """The belief base.
    Initially empty
    beliefBase: A list containing the beliefs
    """
    beliefBase: List[String]
    
    def __init__(self):
        self.beliefBase = [] #[None for _ in range(size)] ?
        
        
    def add(self, sequence):
        #Convert beliefs
        sequence = to_cnf(sequence)
        
        if is_valid(sequence):
            self.beliefBase.add(sequence)
    
    def is_valid(sequence):
        """Check the validity of the input sequence"""
        return 1