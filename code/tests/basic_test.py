
from ..agent.agent import Agent
from ..agent.world import World, Worlds
from ..agent.beliefbase import Belief


def test_basic_create():
    # Some basic creation of the system, not implemented yet, so cant directly call
    agent = Agent()


def test_revision():
    agent = Agent([('p'), ('q'), ('p>>q')])
    assert len(agent.belief_base.beliefBase.keys()) == 3
    agent.belief_base.revise('~q')
    assert len(agent.belief_base.beliefBase) == 2


#if we try to remove belief from base, none of the beliefs in base will entail the belief after contraction.
def test_contraction_closure():
    #knowledge base is p,q,p->q,r contract q : Cn(p,r) or Cn(p>>q,r) 
    agent = Agent([('p'),('q'), ('p>>q'),('r')])
    new_belief = Belief('q')
    agent.belief_base.contract(new_belief)
    assert agent.belief_base.resolution(new_belief)    

#if the belief is removed it works.
def test_contraction_success():
    #knowledge base is p, p->q,r contract r : Cn(p,p->q)
    #pass if r isn't in the belief base
    
    agent = Agent([('p'),('q'), ('p>>q'),('r')])
    new_belief = Belief('r')
    agent.belief_base.contract(new_belief)
    a : bool
    a = true
    for key, belief in agent.belief_base.beliefBase:
        if key=='r':
            a = false
        
    assert a

#check that the result is a subset of the original beliefbase.
def test_contraction_inclusion():
    #knowledge base is p, p->q,r contract r : Cn(p,p->q)
    #pass if there are no new beliefs right?
    agent = Agent([('p'),('q'), ('p>>q'),('r')])
    new_belief = Belief('r')
    agent.belief_base.contract(new_belief)
    
    pass

#test that the base didn't change
def test_contraction_vacuity():
    #knowledge base is p, p->q contract r : Cn(p,p->q)
    #pass if there is no change.
    agent = Agent([('p'),('q'), ('p>>q')])
    new_belief = Belief('r')
    agent.belief_base.contract(new_belief)
    
    pass


def test_contraction_extensionality():
    #do 10 times
    #knowledge base is p, p<->q,r contract p<->q : Cn(p,r)
    #do once knowledge base is p, p<->q,r contract p->q & q->p : Cn(p,r)
    for x in range(10):
        agent = Agent([('p'),('q'), ('p>>q'),('r')])
        new_belief = Belief('q')
        agent.belief_base.contract(new_belief)
    #pass if all created belief bases are equivalent
    pass

#it's not really possible to test recovery but our function should by definition make sure this postulate holds true.
def test_contraction_recovery():
    #how would i test this?
    pass

#if we add a belief there should be no contradictions in the knowledge base.
def test_revision_closure():
    
    pass

#beliefs are added succesfully.
def test_revision_success():
    
    pass

#the outcome is a subset of the union between starting belief base and the new belief.
def test_revision_inclusion():
    
    pass

#nothing should be removed if none of the current beliefs contradict the new belief.
def test_revision_vacuity():
    
    pass

#you should get the same result when doing revision with the same beliefbase and the same new belief
def test_revision_consistency():
    
    pass

#not sure how to test this? 
def test_revision_superexpansion():
    
    pass

#not sure how to test this? 
def test_revision_subexpansion():
    
    pass

def test_worlds():
    test = Worlds()
    test.create_worlds("p&p>>q|t", ["p", "q", "t"])
    assert len(test.worlds_list) == 2**3
    test.create_worlds("a&b&c&d&e&f&g&h", ["a", "b", "c", "d", "e", "f", "g", "h"])
    assert len(test.worlds_list) == 2**8
