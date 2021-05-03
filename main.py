from code.agent import BeliefBase
from sympy.logic.boolalg import to_cnf, And, Or, Not

if __name__ == "__main__":
    bb = BeliefBase()
    while True:
        print('Current belief base:')
        bb.display_belief()
        var = input("Please add to the belief base: ")
        if var.lower() == "quit" :  #   If the input is quit break (adin)
            break
        try:   #   use sympy to check if the var contains the correct language (adin)
            to_cnf(var)
        except:
            print("The input is invalid.")    
        #   if the language is correct convert the belief base into sympy and do revision.
        
        #   Check entailment with negated belief to check if the belief base contradicts your new belief.
        #   if it isn't entailed contract from the belief base then add belief.
        #   There shouldn't be any duplicate beliefs.
        
        
        
        
        #Entailment
        #check if belief base entails negated belief. If not then add belief to base. 
        #If it is entailed then contract beliefs until the negation isn't entailed, then add belief.