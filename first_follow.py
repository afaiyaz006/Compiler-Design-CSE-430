from left_recursion_elimination_algorithm import remove_left_recursion


def find_first(grammer:dict[str:str]):
    nonterminals=list(grammer.keys())
    reversed(nonterminals)
    firsts=set()
    firsts_dict={k:None for k in nonterminals}
    def first_(key):
        
        for production in grammer[key]:
            pointer=0
            while(pointer<len(grammer[key])):
                first_char=production[pointer][0]
                if first_char in nonterminals:
                    if '∈' in grammer[first_char]:
                        pointer+=1

                    

            else:
                firsts.add(production[0])
        return firsts
    
    for nonterminal in nonterminals:
        #print(f"{nonterminal}: {first_(nonterminal)}")
        firsts_dict[nonterminal]=first_(nonterminal)
        firsts=set()
    return firsts_dict



    




if __name__=='__main__':
    grammers="""
###
S->aBDh,
B->cC,
C->bC|∈,
D->EF,
E->g|∈,
F->f|∈
###
"""
    grammers=grammers.replace('\n','')
    grammers=grammers.split("###")
   
    for grammer in grammers:
        if grammer!='':
            grammer=remove_left_recursion(grammer)
            print(grammer)
            print(find_first(grammer))