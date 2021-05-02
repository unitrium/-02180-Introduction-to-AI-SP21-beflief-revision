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
        self.cnf = to_cnf(formula)


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

    def resolution(self, alpha: Belief) -> bool:
    """Resolution Algorithm for propositional logic"""
    """Figure 7.12 in the book"""

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

        disci = dissociate(ci, Or)
        discj = dissociate(cj, Or)

        for i in disci:
            for j in discj:
                if i == ~j or ~i == j:
                    result = removeall(i, disci) + removeall(j, discj)
                    result = unique(result)

                    assresult = associate(result, Or)

                    clauses.append(assresult)

        return resclauses

    def dissociate(clause, operator) -> list:
        """Return a and b separately according to
        the operator when the input is a & b or a | b"""

        disclause = []

        return disclause

    def associate(clause, operator):
        """According to the input operator return a & b or a | b"""

        assclause = []

        return assclause
