"""Class for defining the Agent"""
from typing import List, Tuple
from .beliefbase import BeliefBase


class Agent:
    belief_base: BeliefBase

    def __init__(self, init_beliefs: List[Tuple[str, int]] = []) -> None:
        self.belief_base = BeliefBase()
        if len(init_beliefs) > 0:
            for belief, priority in init_beliefs:
                self.belief_base.revise(belief, priority)
        print('Your belief base is:')
        self.display()

    def display(self) -> None:
        """Display the belief Base"""
        self.belief_base.display_belief()

    def ask_action(self):
        """Ask the human for an action."""
        print("What do you want to do ?")
