"""Class for defining the Belief Base"""
from sympy.logic.boolalg import to_cnf
from typing import List
from .agent import Agent, Action

class BeliefBase:
    """The belief base.
    Initially empty
    beliefBase: A list containing the beliefs
    """
    beliefBase: dict

    def __init__(self):
        self.beliefBase = {}


    def add(self, sequence):
        #Convert beliefs
        converted = to_cnf(sequence)

        if is_valid(sequence):
            self.beliefBase[sequence] = converted

    def is_valid(sequence):
        """Check the validity of the input sequence"""
        return 1

    def display_belief(self) -> None:
        print(belief) for belief in self.beliefBase.keys()
