"""Class for defining the Agent"""
from typing import List
from abc import ABC, abstractmethod


class Action:
    x: str #Add or remove a sequence or display the belief base
    y: str #sequence to add or remove

class Agent:
    
    def __init__(self) -> None:
        
        
        
    def display(self, beliefBase: List[str]) -> None:
        """Display the belief Base"""
        print("Belief Base")
        print()
        print(beliefBase)
        
        
    def ask_action(self) -> Action:
        """Ask the human for an action."""
        print("What do you want to do ?")