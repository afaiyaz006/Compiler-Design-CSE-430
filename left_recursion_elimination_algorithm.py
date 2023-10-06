def remove_left_recursion(grammer:str)->dict[str:str]:
    """
    Removes left recursion from grammer.
    input:
        grammer: a grammer string in comma seprated format i.e: A->AB,A->B|d,B->d.
        
    output: 
        dict[key(str):value(str)]: dictionary containing nonterminal->production

    Algorithm:
        for i=1 to n:
            for j=1 to i-1:
                replace production in the format Ai->Ajγ
                by productions Ai->δ1γ|δ2γ|δ3γ....|δkγ
                where Aj-> δ1|δ2|δ3....|δk current
            eliminate the immediate left recursion of the Aj
            productions.

    """
    rules=grammer.split(',')
    rules=[rule.split('->') for rule in rules]
    rules={k:v.split('|') for k,v in rules}

    nonterminals=list(rules.keys())
    #print(nonterminals)
    for i in range(0,len(nonterminals)):
        Ai=nonterminals[i]
        for j in range(0,i):
            '''
            replacing production in the format Ai->Ajγk
            with  Ai->δ1γk|δ2γk|δ3γk....|δkγk
            '''
            Aj=nonterminals[j]
            new_production=[]
            for production in rules[Ai]: #iterating  the productions of Ai to find γk
                if production[0]==Aj:
                    for prod in rules[Aj]: # iterating the productions of Aj to find δ1,δ2,.....δk
                        new_production.append(prod+production[1:]) #Ai->δ1γk|δ2γk|δ3γk....|δkγk
                else:
                    new_production.append(production) # no change i.e: Ai-> whatever it was before
            
            if len(new_production)>0: # paranoia
                rules[Ai]=new_production

        new_production=[]
        '''
        removing immediate left recursion
        '''
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
                        rules[Ai_prime]=[rule[1:]+Ai_prime,'∈']
                    else:
                        rules[Ai_prime].append(rule[1:]+Ai_prime)
            rules[Ai]=new_production

    return rules     
 
if __name__=='__main__':
    grammers="""
###
E->E+T|T
###
T->T*F|F,
F->∈
###
S->01A,
A->0S1SA|∈
###
S->A,
A->Ad|Ae|aB|ac,
B->bBc|f
###
S->Aa|b,
A->Ac|Aad|bd|∈
###
E->E+T|T,
T->T*F|F,
F->(E)|id
###
S->Af|b,
A->Ac|Sd|Be,
B->Ag|Sh|k
###
S->Af|b,
A->Ac|Sd|Be|C,
B->Ag|Sh|k,
C->BkmA|AS|j
###
Q->QED|q,
E->e,
D->NFA|d,
N->DFA|n,
F->f,
A->a
"""

    grammers=grammers.replace('\n','')
    grammers=grammers.split("###")
    
    for grammer in grammers:
        if grammer!='':
            print("---Grammer with left recursion---")
            for production in grammer.split(','):
                print(production)
            print("---------------------------------")
            
            print("---Grammer without left recursion---")
            grammer_without_left_recursion=remove_left_recursion(grammer)
            for nonterminal,productions in grammer_without_left_recursion.items():
                print(f"{nonterminal}->{'|'.join(productions)}")
            print("------------------------------------")