"""Class for defining the Worlds"""
from typing import List, Tuple
from sympy import *



class World:
    probability: int
    world_data: str

    def __init__(self, probability: float, world_data: str) -> None:
        self.probability = probability
        self.world_data = world_data

class Worlds:
    worlds_list: List[World]

    def __init__(self) -> None:
        self.worlds_list = []

    def add_to_tail(self, world: World):
        self.worlds_list.append(world)

    def add_to_head(self, world: World):
        self.worlds_list.insert(0, world)

    def rearrange_world(self, old_index: int, new_index: int):
        self.worlds_list.insert(new_index, self.worlds_list.pop(old_index))

    def get_first_world(self) -> World:
        if len(self.worlds_list) > 0:
            return self.worlds_list.pop(0)
        return None

    def sort_worlds(self):
        self.worlds_list.sort(key=self.sort_function)

    def sort_function(self, element: World):
        return element.probability

    def print_worlds(self):
        for element in self.worlds_list:
            print("Element with probability: "+str(element.probability)+" and data: "+str(element.world_data))

    def create_worlds(self, collective_beliefs, variables_in_base):
        self.worlds_list = []
        #Use Sympy with simplify to get the form
        result = to_cnf(collective_beliefs, True)
        converted_result = str(result)

        #Setup variables for algorithm to create worlds
        old_variables = variables_in_base[:]
        variable_length = len(variables_in_base)
        total_worlds = 2**variable_length

        #Iterate over all the worlds, which is 2^n, with n = AMOUNT_OF_VARIABLES
        for i in range(total_worlds):
            new_world = converted_result
            #Iterate over the different types of variables, and negate them if nesiarry to get all possible worlds
            for j in range(variable_length):
                old_variable = variables_in_base[j]
                if i % 2**(variable_length - j - 1) == 0 and i != 0:
                    if "~" in variables_in_base[j]:
                        variables_in_base[j] = variables_in_base[j].replace("~", "")
                    else:
                        variables_in_base[j] = "~"+variables_in_base[j]
                new_world = new_world.replace(old_variables[j], variables_in_base[j])
            world_object = World(total_worlds-i, new_world)
            self.add_to_tail(world_object)
