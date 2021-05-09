"""Class for defining the Belief Base"""
from sympy.logic.boolalg import to_cnf, And, Or, Not
from typing import Dict


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
        # Convert beliefs
        belief = Belief(sequence, 0)
        if self.is_valid(belief):
            self.beliefBase[sequence] = belief

    def is_valid(self, belief):
        """Check the validity of the input sequence"""
        if self.beliefBaseVariableLimit == -1:
            return true
        """Check if new variables has been added, if yes, check if still within limit"""
        variablesInBelief = []
        for char in belief.formula:
            char_value = ord(char)
            if char_value >= 65 and char_value <= 90 or char_value >= 97 and char_value <= 122:
                if char not in variablesInBelief:
                    variablesInBelief.append(char)
        variablesInBase = self.variables_in_base()
        for element in variablesInBelief:
            if element not in variablesInBase:
                variablesInBase.append(element)
        if len(variablesInBase) > self.beliefBaseVariableLimit:
            return False
        return True

    def variables_in_base(self):
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
        if not self._contract(new_belief):
            print(f'adding new belief {new_belief}')
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
        for key, belief in self.beliefBase.items():
            if Or(Not(belief.cnf), Not(new_belief.cnf)):
                if belief.priority < new_belief.priority:
                    to_remove.append(key)
                else:
                    incompatibility = True
        for key in to_remove:
            print(f'Pop {key}')
            self.beliefBase.pop(key)
        return incompatibility

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
