"""Class for defining the Worlds"""
from typing import List, Tuple


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
            print("Element with probability: "+str(element.probability) +
                  " and data: "+str(element.world_data))


test = Worlds()
test.add_to_head(World(3, ""))
test.add_to_head(World(4, ""))
test.add_to_head(World(2, ""))
test.add_to_head(World(9, ""))
test.add_to_head(World(1, ""))
test.print_worlds()
print("")
test.rearrange_world(0, 1)
test.print_worlds()
print("")
test.sort_worlds()
test.print_worlds()
print("")
test.add_to_tail(World(100, "haha"))
test.add_to_head(World(100, "hihi"))
test.print_worlds()
