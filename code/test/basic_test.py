import pytest
from ..agent import agent, beliefbase


def test_basic_create():
    #Some basic creation of the system, not implemented yet, so cant directly call
    b = beliefbase(?)
    agent = agent()

def test_adding():
    #some beliefbase b
    #Test that checks that it a "real" belief can be added and is added
    beliefSize = b.getSize()
    b.addBelief("p")
    currentBeliefSize = b.getSize()
    assert currentBeliefSize - beliefSize == 1
    #Test that checks that if you input not "real" belief it will be disregarded and not added
    b.addBelief("sdkfmg9nw345#¤%!.-3!")
    assert b.getSize() == currentBeliefSize
    #Test that checks if you add the same belief twice it doesn't get added
    b.addBelief("p")
    assert b.getSize() == currentBeliefSize

def test_removing():
    #some beliefbase b
    #Test that removing a valid belief will actually remove it
    assert b.containsBelief("p")
    b.removeBelief("p")
    assert not b.containsBelief("p")
    beliefSize = b.getSize()
    b.removeBelief("p")
    assert beliefSize == b.getSize()

def test_beliefbase():
    #some beliefbase b
    b.addBelief("p")
    b.addBelief("q")
    b.addBelief("p->q")
    assert b.computeBeliefs() == "write after knowing syntax"

def test_agent():
    agent something something
