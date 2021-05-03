"""Class for defining the Belief Base"""
from sympy.logic.boolalg import to_cnf, And, Or, Not
from typing import Dict
from .agent import Agent, Action


class Belief:
    cnf: str
    priority: int
    formula: str

    def __init__(self, formula: str, priority: int) -> None:
        self.priority = priority
        self.formula = formula
        self.cnf = to_cnf(formulae)


class BeliefBase:
    """The belief base.
    Initially empty
    beliefBase: Dict containing the beliefs believed to be true,
    the beliefs are referenced by the formulae entered by the user.
    """

    beliefBaseVariableLimit: int

    beliefBase: Dict[Belief]

    def __init__(self):
        self.beliefBase = {}
        beliefBaseVariableLimit = 8

    def add(self, sequence):
        # Convert beliefs
        belief = Belief(sequence, 0)
        if is_valid(belief):
            self.beliefBase[sequence] = belief


        """Check the validity of the input sequence"""
        if beliefBaseVariableLimit == -1:
            return true
        """Check if new variables has been added, if yes, check if still within limit"""
        variablesInBelief = []
            char_value = ord(char)
            if char_value >= 65 and char_value <= 90 or char_value >= 97 and char_value <= 122:
                if char not in variablesInBelief:
                    variablesInBelief.append(char)
        variablesInBase = variables_in_base()
        for element in variablesInBelief:
            if element not in variablesInBase:
                variablesInBase.append(element)
        if len(variablesInBase) > beliefBaseVariableLimit:
            return false
        return True

    def variables_in_base(self) -> int:
        """Count the variables in the beliefbase"""
        list = []
        for belief in self.beliefBase.keys():
            for char in belief:
                char_value = ord(char)
                if char_value >= 65 and char_value <= 90 or char_value >= 97 and char_value <= 122:
                    if char not in list:
                        list.append(char)
        return list

    def display_belief(self) -> None:
        for belief in self.beliefBase.keys():
            print(belief)

    def revise(self, new_formulae: str, priority: int):
        new_belief = Belief(new_formulae, priority)
        if self._contract(new_belief):
            self._expand(new_belief)

    def _expand(self, new_belief: Belief):
        self.beliefBase[new_belief.formula] = new_belief

    def _contract(self, new_belief: Belief) -> bool:
        """Contracts the belief base. It is assumed that the new belief is not a tautology.
        Returns a boolean on wether the new belief is compatible with existing beliefs
        given the priority.
        """
        to_remove = []
        incompatibility = False
        for key, belief in enumerate(self.beliefBase):
            if And(belief.cnf, Not(new_belief.cnf)):
                if belief.priority < new_belief.priority:
                    to_remove.append(key)
                else:
                    incompatibility = True
        for key in to_remove:
            self.beliefBase.pop(key)
        return incompatibility
