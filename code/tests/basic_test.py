import pytest
from ..agent.agent import Agent
from ..agent.world import World, Worlds

def test_basic_create():
    # Some basic creation of the system, not implemented yet, so cant directly call
    agent = Agent()


def test_revision():
    agent = Agent([('p'), ('q'), ('p>>q')])
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
    test.create_worlds("p&p>>q|t", ["p", "q", "t"])
    aasert len(test.worlds_list) == 2**3
    test.create_worlds("a&b&c&d&e&f&g&h", ["a", "b", "c", "d", "e", "f", "g", "h"])
    aasert len(test.worlds_list) == 2**8
