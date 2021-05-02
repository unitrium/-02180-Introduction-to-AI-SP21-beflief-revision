import pytest
from ..agent import 


def test_basic_create():
    #Some basic creation of the system, not implemented yet, so cant directly call
    b = BeliefBase()
    agent = Agent()

def test_adding():
    #some beliefbase b
    #Test that checks that it a "real" belief can be added and is added
    beliefSize = b.getSize()
    b.add("p")
    currentBeliefSize = b.getSize()
    assert currentBeliefSize - beliefSize == 1
    #Test that checks that if you input not "real" belief it will be disregarded and not added
    b.add("sdkfmg9nw345#¤%!.-3!")
    assert b.getSize() == currentBeliefSize
    #Test that checks if you add the same belief twice it doesn't get added
    b.add("p")
    assert b.getSize() == currentBeliefSize

def test_removing():
    #some beliefbase b
    #Test that inversing a valid belief that exists will actually remove it
    assert b.containsBelief("p")
    b.add("!p")
    assert not b.containsBelief("p")
    beliefSize = b.getSize()
    b.add("!p")
    assert beliefSize != b.getSize()

def test_beliefbase():
    #some beliefbase b
    b.add("p")
    b.add("q")
    b.add("p->q")
    assert b.computeBeliefs() == "write after knowing syntax"
