import pytest
from ..agent.agent import Agent
from ..agent.world import World, Worlds

def test_basic_create():
    # Some basic creation of the system, not implemented yet, so cant directly call
    agent = Agent()


def test_revision():
    agent = Agent([('p', 1), ('q', 2), ('p>>q', 3)])
    assert len(agent.belief_base.beliefBase.keys()) == 3
    agent.belief_base.revise('~q', 1)
    assert len(agent.belief_base.beliefBase) == 2


def test_contraction_closure():
    pass


def test_contraction_success():
    pass


def test_contraction_inclusion():
    pass


def test_contraction_vacuity():
    pass


def test_contraction_extensionality():
    pass


def test_contraction_recovery():
    pass

def test_worlds():
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
    test.add_to_tail(World(100,"haha"))
    test.add_to_head(World(100,"hihi"))
    test.print_worlds()
    test.create_worlds("p&p>>q|t", ["p", "q", "t"])
    test.print_worlds()
    pass

test_worlds()
