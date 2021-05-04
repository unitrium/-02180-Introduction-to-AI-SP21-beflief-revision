import pytest
from ..agent.agent import Agent
from ..agent.beliefbase import BeliefBase


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
