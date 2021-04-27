from code.agent import BeliefBase


if __name__ == "__main__":
    bb = BeliefBase()
    while True:
        print('Current belief base:')
        bb.display_belief()
        var = input("Please add to the belief base: ")
        
        #   If the input is quit break (adin)
        #   use sympy to check if the var contains the correct language (adin)
        #   if the language is correct convert the belief base into sympy and do revision.
        
        #   Check entailment with negated belief to check if the belief base contradicts your new belief.
        #   if it isn't entailed contract from the belief base then add belief.
        #   There shouldn't be any duplicate beliefs.