def left_recursion_removal(grammer:str)->str:
    """
    Removes the left recursion of a given grammer.
    """
    rules=grammer.split(',')
    new_rules=[]
    
    for rule in rules:
        #print(rule)
        nonterminal,productions=rule.split('->')
        productions=productions.split('|')
        immediates=set()
        for rule in productions:
            if nonterminal==rule[0]:
                new_rule=f"{nonterminal}'->{rule[1:]}{nonterminal}'|ε"
                #print(new_rule)
                immediates.add(nonterminal)
                new_rules.append(new_rule+"\n")
            else:
                if nonterminal not in immediates:
                    new_rule=f"{nonterminal}->{rule}"
                    new_rules.append(new_rule+"\n")
                
        for immediate in list(immediates):
            for rule in productions:
                if immediate not in rule:
                    new_rule=f"{immediate}->{rule}{immediate}'"
                   #print(new_rule)
                    new_rules.append(new_rule+"\n")
    new_rules.reverse()
    return new_rules
                        
        
    




if __name__=='__main__':
    grammers="""
###
E->E+T|T
###
T->T*F|F
###
S->Aa|b,
A->Ac|Aad|bd|ε
###
E->E+T|T,
T->T*F|F,
F->(E)|id
"""#Examples taken from:#https://www.csd.uwo.ca/~mmorenom/CS447/Lectures/Syntax.html/node8.html

    grammers=grammers.replace('\n','')
    grammers=grammers.split("###")
    
    for grammer in grammers:
        if grammer!='':
            print("#####")
            print("Without left recursion removal:")
            print("\n".join(grammer.split(',')))
            print(".......")
            print("After left recursion removal:")
            grammer=left_recursion_removal(grammer)
            print("".join(grammer))
            