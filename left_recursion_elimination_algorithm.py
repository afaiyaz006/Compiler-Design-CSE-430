def remove_left_recursion(grammer:str)->dict[str:str]:
    rules=grammer.split(',')
    rules=[rule.split('->') for rule in rules]
    rules={k:v.split('|') for k,v in rules}
    nonterminals=list(rules.keys())
    #print(nonterminals)
    for i in range(0,len(nonterminals)):
        Ai=nonterminals[i]
        for j in range(0,i):
            Aj=nonterminals[j]
            new_production=[]
            for production in rules[Ai]:
                if production[0]==Aj:
                    for prod in rules[Aj]:
                        new_production.append(prod+production[1:])
                else:
                    new_production.append(production)

            if len(new_production)>0:
                rules[Ai]=new_production
        new_production=[]
        immediate=False
        for rule in rules[Ai]:
            if rule[0]==Ai:
                immediate=True
                break
        if immediate:
            for rule in rules[Ai]:
                if rule[0]!=Ai:
                    new_production.append(f"{rule}{Ai}'")
                elif rule[0]==Ai:
                    Ai_prime=f"{Ai}'"
                    if Ai_prime not in rules:
                        rules[Ai_prime]=[rule[1:]+Ai_prime]
                    else:
                        rules[Ai_prime].append(rule[1:]+Ai_prime)
            rules[Ai]=new_production
    return rules      
if __name__=='__main__':
    grammers="""
###
E->E+T|T,
T->ε
###
T->T*F|F,
F->ε
###
S->Aa|b,
A->Ac|Aad|bd|ε
###
E->E+T|T,
T->T*F|F,
F->(E)|id
###
S->Af|b,
A->Ac|Sd|Be|C,
B->Ag|Sh|k,
C->BkmA|AS|j
"""
#Examples taken from:#https://www.csd.uwo.ca/~mmorenom/CS447/Lectures/Syntax.html/node8.html

    grammers=grammers.replace('\n','')
    grammers=grammers.split("###")
    
    for grammer in grammers:
        if grammer!='':
            print("-----")
            grammer_without_left_recursion=remove_left_recursion(grammer)
            for nonterminal,productions in grammer_without_left_recursion.items():
                print(f"{nonterminal}->{'|'.join(productions)}")
            print("-----")