"""Class for defining the Belief Base"""
from sympy.logic.boolalg import to_cnf, And, Or, Not
from typing import Dict, List
from copy import deepcopy


class Belief:
    cnf: str
    priority: int
    formula: str

    def __init__(self, formula: str, priority: int) -> None:
        self.priority = priority
        self.formula = formula
        self.cnf = to_cnf(formula)


class BeliefBase:
    """The belief base.
    Initially empty
    beliefBase: Dict containing the beliefs believed to be true,
    the beliefs are referenced by the formula entered by the user.
    """
    beliefBase: dict
    beliefBaseVariableLimit: int

    def __init__(self):
        self.beliefBase = {}
        self.beliefBaseVariableLimit = 8

    def add(self, sequence):
        """Add a sequence to the belief base."""
        belief = Belief(sequence, 0)
        if self.is_valid(belief):
            self.beliefBase[sequence] = belief

    def clear(self):
        """Clears the belief base."""
        self.beliefBase = {}

    def is_valid(self, belief):
        """Check if new variables has been added, if yes, check if still within limit"""
        if self.beliefBaseVariableLimit == -1:
            return True
        variablesInBelief = []
        for char in belief.formula:
            char_value = ord(char)
            if char_value >= 65 and char_value <= 90 or char_value >= 97 and char_value <= 122:
                if char not in variablesInBelief:
                    variablesInBelief.append(char)
        variablesInBase = self.variables_in_base()
        variablesInBase += [var for var in variablesInBelief if var not in variablesInBase]
        if len(variablesInBase) > self.beliefBaseVariableLimit:
            return False
        return True

    def variables_in_base(self):
        """Count the variables in the beliefbase"""
        variables = []
        for belief in self.beliefBase.keys():
            for char in belief:
                if char not in variables:
                    char_value = ord(char)
                    if char_value >= 65 and char_value <= 90 or char_value >= 97 and char_value <= 122:
                        variables.append(char)
        return variables

    def display_belief(self) -> None:
        for belief in self.beliefBase.keys():
            print(belief)

    def revise(self, new_formulae: str, priority: int):
        new_belief = Belief(new_formulae, priority)
        if not self._contract(new_belief):
            print(f'adding new belief {new_belief}')
            self._expand(new_belief)

    def _expand(self, new_belief: Belief):
        self.beliefBase[new_belief.formula] = new_belief

    def _contract(self, new_belief: Belief) -> bool:
        """Contracts the belief base. It is assumed that the new belief is not a tautology.
        Does a graph search to remove all the beliefs until it doesn't contradict anymore.
        """
        beliefBase = deepcopy(self.beliefBase)
        contradiction = True
        queue = [beliefBase]
        index = 0
        while contradiction:
            to_remove = []
            contradiction = False
            for belief in queue[index]:
                if Or(Not(belief.cnf), Not(new_belief.cnf)):
                    new_state = deepcopy(beliefBase)
                    new_state.beliefBase.pop(belief.formula)
                    queue.append(new_state)
                    contradiction = True
            if contradiction:
                index += 1
        self.beliefBase = queue[index]

    def resolution(self, alpha: Belief) -> bool:
        """Resolution Algorithm for propositional logic.
        Figure 7.12 in the book
        """

        clauses = []  # Clauses is the set of clauses in the CNF representation of KB A !alpha
        # Formalisaiton of KB as CNF
        for kb in self.beliefBase.keys():
            clauses.append(self.dissociate(kb, And))

        # Add CNF of the contradiction of alpha
            clauses.append(self.dissociate(to_cnf(~alpha.cnf), And))

        if False in clauses:
            return True

        new = set()
        while True:
            n = len(clauses)
            pairs = [(clauses[i], clauses[j])
                     for i in range(n) for j in range(i+1, n)]

            for ci, cj in pairs:
                res = self.resolve(ci, cj)
                if False in res:
                    # Empty clause
                    return True
                new = new.union(set(res))

            if new.issubset(set(clauses)):
                return False

            for c in new:
                if c not in clauses:
                    clauses = clauses.append(new)

    def resolve(self, ci, cj) -> list:
        """Returns the set of all possible clauses
        obtained by resolving its two inputs ci and cj"""

        resclauses = []

        disci = self.dissociate(ci, Or)
        discj = self.dissociate(cj, Or)

        for i in disci:
            for j in discj:
                if i == ~j or ~i == j:
                    result = removeall(i, disci) + removeall(j, discj)
                    result = unique(result)

                    assresult = self.associate(result, Or)

                    clauses.append(assresult)

        return resclauses

    def dissociate(self, clause, operator) -> list:
        """Return a and b separately according to
        the operator when the input is a & b or a | b"""

        disclause = []

        return disclause

    def associate(self, clause, operator):
        """According to the input operator return a & b or a | b"""

        assclause = []

        return assclause
