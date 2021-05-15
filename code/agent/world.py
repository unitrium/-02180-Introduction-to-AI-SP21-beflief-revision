"""Class for defining the Worlds"""
from typing import List, Tuple
from sympy import *

class World:
    world_data: str

    def __init__(self, world_data: str) -> None:
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

    def print_worlds(self):
        i = 1
        for element in self.worlds_list:
            print("Element in FIFO queue #: "+str(i)+
                  " with data: "+str(element.world_data))
            i += 1

    def create_worlds(self, collective_beliefs, variables_in_base):
        """Function to create 2^n worlds, with n being the amount of variables_in_base.
        It creates the worlds_list based on the collective_beliefs argument using simplify."""
        self.worlds_list = []
        result = to_cnf(collective_beliefs, True)
        converted_result = str(result)

        old_variables = variables_in_base[:]
        variable_length = len(variables_in_base)
        total_worlds = 2**variable_length

        for i in range(total_worlds):
            new_world = converted_result
            for j in range(variable_length):
                old_variable = variables_in_base[j]
                if i % 2**(variable_length - j - 1) == 0 and i != 0:
                    if "~" in variables_in_base[j]:
                        variables_in_base[j] = variables_in_base[j].replace("~", "")
                    else:
                        variables_in_base[j] = "~"+variables_in_base[j]
                new_world = new_world.replace(old_variables[j], variables_in_base[j])
            world_object = World(new_world)
            self.add_to_tail(world_object)
