"""Class for defining the Belief Base"""
from sympy.logic.boolalg import to_cnf, Not
from typing import List

from .world import Worlds


class Belief:
    cnf: str
    formula: str

    def __init__(self, formula: str) -> None:
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

    def __copy__(self) -> "BeliefBase":
        """Return a deep copy of the belief base to be used as a new state."""
        new_bb = BeliefBase()
        for key, belief in self.beliefBase.items():
            new_bb.beliefBase[key] = Belief(belief.formula)
        return new_bb

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

    def variables_in_base(self) -> List[str]:
        """Lists the variables in the beliefbase"""
        variables = []
        for belief in self.beliefBase.keys():
            for char in belief:
                if char not in variables:
                    char_value = ord(char)
                    if char_value >= 65 and char_value <= 90 or char_value >= 97 and char_value <= 122:
                        variables.append(char)
        return variables

    def _collective_beliefs(self) -> str:
        """Concatenates all the beliefs in belief base in their cnf with &."""
        return str(to_cnf('&'.join(
            [str(belief.cnf) for belief in self.beliefBase.values()]), True))

    def _create_worlds(self) -> Worlds:
        worlds = Worlds()
        worlds.create_worlds(self._collective_beliefs(),
                             self.variables_in_base())
        return worlds

    def get_plausibility(self) -> int:
        collective_beliefs = self._collective_beliefs()
        for index, world in enumerate(self._create_worlds().worlds_list):
            if world.world_data == collective_beliefs:
                return index

    def display_belief(self) -> None:
        for belief in self.beliefBase.keys():
            print(belief)

    def revise(self, new_formula: str):
        """Function to add a new belief to the belief base with consistency."""
        new_belief = Belief(new_formula)
        not_new_belief = Belief(f'~({new_belief.cnf})')
        self.contract(not_new_belief)
        print(f'adding new belief {new_belief.formula}')
        self._expand(new_belief)

    def _expand(self, new_belief: Belief):
        self.beliefBase[new_belief.formula] = new_belief

    def contract(self, new_belief: Belief) -> None:
        """Contracts the belief base. It is assumed that the new belief is not a tautology.
        Does a graph search to remove all the beliefs until it doesn't contradict anymore.
        """
        if len(self.beliefBase.keys()) == 0:
            return
        beliefBase = self.__copy__()
        contradiction = True
        queue = [beliefBase]
        while contradiction:
            possible_belief_bases = []
            contradiction = False
            current_belief_base = queue.pop(0)
            for belief in current_belief_base.beliefBase.values():
                if current_belief_base.resolution(new_belief):
                    new_state = current_belief_base.__copy__()
                    new_state.beliefBase.pop(belief.formula)
                    queue.append(new_state)
                    contradiction = True
                else:
                    possible_belief_bases.append(current_belief_base)
                    break
        if len(queue) > 0:
            alternative_belief_base = queue.pop(0)
            while len(alternative_belief_base.beliefBase) == len(possible_belief_bases[0].beliefBase):
                possible_belief_bases.append(alternative_belief_base)
                if len(queue) > 0:
                    alternative_belief_base = queue.pop(0)
                else:
                    break
        if len(possible_belief_bases) == 0:
            self.beliefBase.clear()
            return
        best_plausibility_order = possible_belief_bases[0].get_plausibility()
        self.beliefBase = possible_belief_bases[0].beliefBase
        for beliefBase in possible_belief_bases:
            if best_plausibility_order > beliefBase.get_plausibility():
                self.beliefBase = beliefBase.beliefBase

    def resolution(self, alpha: Belief) -> bool:
        """Resolution Algorithm for propositional logic.
        Check if the belief is entailed in the the belief base.
        Figure 7.12 in the book
        """
        alpha = Belief(f'~({alpha.cnf})')
        clauses = []  # Clauses is the set of clauses in the CNF representation of KB A !alpha
        for belief in self.beliefBase.values():
            for dissociated_belief in self.dissociate(str(belief.cnf), " & "):
                if dissociated_belief[0] == "(":
                    clauses.append(dissociated_belief[1:-1])
                else:
                    clauses.append(dissociated_belief)
        for dissociated_alpha in self.dissociate(str(alpha.cnf), " & "):
            if dissociated_alpha[0] == "(":
                clauses.append(dissociated_alpha[1:-1])
            else:
                clauses.append(dissociated_alpha)
        new = set()
        while True:
            n = len(clauses)
            pairs = [(clauses[i], clauses[j])
                     for i in range(n) for j in range(i+1, n)]

            for ci, cj in pairs:
                res = self.resolve(ci, cj)
                if '' in res:
                    # Empty clause
                    return True

                new = new.union(set(res))

            if new.issubset(set(clauses)):
                return False
            clauses += [clause for clause in new if clause not in clauses]

    def resolve(self, ci, cj) -> list:
        """Returns the set of all possible clauses
        obtained by resolving its two inputs ci and cj"""

        resclauses = []
        disci = self.dissociate(str(ci), " | ")
        discj = self.dissociate(str(cj), " | ")
        for i in disci:
            for j in discj:
                if i == str(Not(j)) or str(Not(i)) == j:

                    result = [rci for rci in self.removeclause(i, disci)]
                    result += [rcj for rcj in self.removeclause(j, discj)]
                    result = list(set(result))
                    assresult = self.associate(result, " | ")
                    resclauses.append(assresult)

        return resclauses

    def dissociate(self, clause: str, operator: str) -> List[str]:
        """Return a and b separately according to
        the operator when the input is a & b or a | b"""
        return clause.split(operator)

    def associate(self, clause: List[str], operator: str) -> str:
        """According to the input operator return a & b or a | b"""
        return operator.join(clause)

    def removeclause(self, c, base):
        return [x for x in base if x != c]
