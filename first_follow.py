from left_recursion_elimination_algorithm import remove_left_recursion


def find_first(grammer:dict[str:list[str]]):
    first_Y={}
    nonterminals=list(grammer.keys())
    nonterminals.reverse()

    for nonterminal,productions in grammer.items():
        for production in productions:
            for symbol in production:
                if symbol not in nonterminals:
                    first_Y[symbol]=set(symbol)
        if '∈' in productions:
            first_Y[nonterminal]=set('∈')
        else:
            first_Y[nonterminal]=set()
        
    del(first_Y['∈'])
   
    for i in range(0,len(nonterminals)**2):
        epsilon_counter=0
        for nonterminal,productions in grammer.items():
            for production in productions:
                for symbol in production:
                   
                    if symbol in nonterminals and '∈' in first_Y[symbol]:
                            epsilon_counter+=1
                            first_Y[nonterminal]=first_Y[nonterminal].union(first_Y[symbol])
                    else:
                        if symbol!='∈':
                            first_Y[nonterminal]=first_Y[nonterminal].union(first_Y[symbol])
                            break
        #if epsilon_counter==0:
        #    break

    return first_Y,nonterminals


def find_follow(grammer:dict[str:list[str]],first_Y:dict[str:set],nonterminals:list[str],start_symbol:str):

    follow_Y={nonterminal:set() for nonterminal in nonterminals}
    follow_Y[start_symbol].add('$')
    
    for steps in range(0,len(nonterminals)**2):
        for nonterminal,productions in grammer.items():
            for production in productions:
                
                for i in range(0,len(production)):
                    
                    if production[i] in nonterminals:
                        Beta=production[i]
                        
                        if i==len(production)-1:
                            follow_Y[Beta]=follow_Y[nonterminal]
                        else:
                            for j in range(i+1,len(production)):
                                if '∈' in first_Y[production[j]]:
                                    follow_Y[Beta]=follow_Y[Beta].union(first_Y[production[j]]).union(follow_Y[nonterminal])
                                else:
                                    follow_Y[Beta]=follow_Y[Beta].union(first_Y[production[j]])
                                    break
    for nonterminal in nonterminals:
       if '∈' in  follow_Y[nonterminal]:
           follow_Y[nonterminal].remove('∈')
    
    return follow_Y


def print_grammer(grammer:dict[str:list[str]]):
    for nonterminal,production in grammer.items():
        print(f"{nonterminal}-> {'|'.join(production)}")


if __name__=='__main__':
    grammers="""
###
E->XTa,
X->+E|∈,
T->iY|(E),
Y->*T|∈
###
S->aBDh,
B->cC,
C->bC|∈,
D->EF,
E->g|∈,
F->f|∈
###
E->TR,
R->+TR|∈,
T->FY,
Y->*FY|∈,
F->(E)|i
###
"""
    grammers=grammers.replace('\n','')
    grammers=grammers.split("###")

    for grammer in grammers:
        if grammer!='':
            
            
            start_symbol=grammer[0]
            grammer=remove_left_recursion(grammer)
            if grammer is not None:
                print("-----------------------------")
                print("Input Grammer: ")
                print_grammer(grammer)
                
                firsts_Y,nonterminals=find_first(grammer)
                nonterminals.reverse()
                
                follow_Y=find_follow(grammer,firsts_Y,nonterminals,start_symbol)
                print("------------------------------")
                for symbol,firsts in firsts_Y.items():
                    if symbol in nonterminals:
                        print(f"First({symbol})-> {firsts_Y[symbol]}")
                print("")
                for symbol,firsts in follow_Y.items():
                    if symbol in nonterminals:
                        print(f"Follow({symbol})-> {follow_Y[symbol]}")
                print("-------------------------------")          