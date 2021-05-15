import pytest
from ..agent.agent import Agent
from ..agent.world import World, Worlds


def test_basic_create():
    # Some basic creation of the system, not implemented yet, so cant directly call
    agent = Agent()


def test_revision():
    agent = Agent([('p'), ('q'), ('p>>q')])
    assert len(agent.belief_base.beliefBase.keys()) == 3
    agent.belief_base.revise('~q')
    assert len(agent.belief_base.beliefBase) == 2


#if we try to remove belief from base the belief none of the beliefs in base will entail the belief after contraction.
def test_contraction_closure():
    #knowledge base is p, p->q,r add ~r : Cn(p,p->q)
    
    pass

#if the belief 
def test_contraction_success():
    #knowledge base is p, p->q,r contract r : Cn(p,p->q)
    #pass if r isn't in the belief base
    
    
    pass


def test_contraction_inclusion():
    #knowledge base is p, p->q,r contract r : Cn(p,p->q)
    #pass if there are no new beliefs right?
    pass


def test_contraction_vacuity():
    #knowledge base is p, p->q add ~r : Cn(p,p->q)
    #pass if there is no change.
    pass


def test_contraction_extensionality():
    #do 10 times
    #knowledge base is p, p<->q,r contract p<->q : Cn(p,r)
    #do once knowledge base is p, p<->q,r contract p->q & q->p : Cn(p,r)
    #pass if all created belief bases are equivalent
    pass


def test_contraction_recovery():
    #how would i test this?
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
    test.add_to_tail(World(100, "haha"))
    test.add_to_head(World(100, "hihi"))
    test.print_worlds()
    test.create_worlds("p&p>>q|t", ["p", "q", "t"])
    test.print_worlds()
    pass


test_worlds()
