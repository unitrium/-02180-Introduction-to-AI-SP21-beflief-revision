"""Class for defining the Belief Base"""
from sympy.logic.boolalg import to_cnf, And, Or, Not
from typing import Dict
from .agent import Agent, Action


class Belief:
    cnf: str
    priority: int

    def __init__(self, formulae: str, priority: int) -> None:
        self.priority = priority
        self.cnf = to_cnf(formulae)


class BeliefBase:
    """The belief base.
    Initially empty
    beliefBase: Dict containing the beliefs believed to be true,
    the beliefs are referenced by the formulae entered by the user.
    """
    beliefBase: Dict[Belief]

    def __init__(self):
        self.beliefBase = {}

    def add(self, sequence):
        # Convert beliefs
        converted = to_cnf(sequence)

        if is_valid(sequence):
            self.beliefBase[sequence] = converted

    def is_valid(sequence):
        """Check the validity of the input sequence"""
        return 1

    def display_belief(self) -> None:
        for belief in self.beliefBase.keys():
            print(belief)

    def __contract(self, new_belief: Belief, priority: int):
        """Contracts the belief base. It is assumed that the new belief is not a tautology."""
        to_remove = []
        for key, belief in enumerate(self.beliefBase):
            if And(belief.cnf, Not(belief.cnf)):
                to_remove.append(key)
        for key in to_remove:
            self.beliefBase.pop(key)
