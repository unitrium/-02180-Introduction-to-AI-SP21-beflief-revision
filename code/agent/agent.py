"""Class for defining the Agent"""
from typing import List, Tuple
from .beliefbase import BeliefBase


class Agent:
    belief_base: BeliefBase
    quit: bool

    def __init__(self, init_beliefs: List[Tuple[str, int]] = []) -> None:
        self.quit = False
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
        print("Select type your action:")
        print('add to add a new belief')
        print('display to display the current belief base')
        print('clear to clear the belief base')
        action = input()
        if action == 'add':
            belief = input('Type your new belief')
            self.belief_base.revise(belief)
            self.display()
        elif action == 'display':
            self.display()
        elif action == 'clear':
            self.belief_base.clear()
        elif action == 'quit':
            self.quit = True
        else:
            print('Unrecognized action.')
