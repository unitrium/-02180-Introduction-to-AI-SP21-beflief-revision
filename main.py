from code.agent import BeliefBase, Agent


if __name__ == "__main__":
    bb = BeliefBase()
    while True:
        print("The current belief base entails"+"Cn{"+"a->b"+","+"a"+"}")
        var = input("Please add to the belief base: ")
        
        #   If the input is quit break (adin)
        #   use sympy to check if the var contains the correct language (adin)
        #   if the language is correct convert the belief base into sympy and do revision.
        
        #   Check entailment with negated belief to check if the belief base contradicts your new belief.
        #   if it isn't entailed contract from the belief base then add belief.
        #   There shouldn't be any duplicate beliefs.
        
        
        
        
        #Entailment
        #check if belief base entails negated belief. If not then add belief to base. 
        #If it is entailed then contract beliefs until the negation isn't entailed, then add belief.