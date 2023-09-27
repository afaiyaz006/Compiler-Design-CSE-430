import streamlit as st
st.set_page_config(page_title="Left Recursion Removal by fuzzy")
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
                        rules[Ai_prime]=[rule[1:]+Ai_prime,'ε']
                    else:
                        rules[Ai_prime].append(rule[1:]+Ai_prime)
            rules[Ai]=new_production
    return rules    



def lr_remover(grammers:str)->str:

    grammers=grammers.replace('\n','')
    grammers=grammers.split("###")
    output=""
    for grammer in grammers:
        if grammer!='':
            
            grammer_without_left_recursion=remove_left_recursion(grammer)
            output+="```\n"
            for nonterminal,productions in grammer_without_left_recursion.items():
                output+=f"{nonterminal}->{'|'.join(productions)}\n"
            output+="```\n"
    return output

if __name__=='__main__':
    st.title(f'Left Recursion Remover :tea: :disappointed_relieved:')
    

with st.form(key="Input Grammer"):
    grammers="""S->Af|b,
A->Ac|Sd|Be|C,
B->Ag|Sh|k,
C->BkmA|AS|j
"""
    #grammers.replace('###','\n')    
    text_input=st.text_area(label="Enter Grammer",value=grammers)
    submit_button=st.form_submit_button(label="Remove Left Recursion")

if submit_button:
    text_output=lr_remover(text_input)
    st.write(text_output)
st.header("Instructions: ")
st.write("""
```
Input format:
###\n
S->A,\n
A->Ad|Ae|aB|ac,\n
B->bBc|f\n
###\n
A->BC,\n
B->ε,\n
###\n
another grammer
Note: Must use comma for new line in grammer
```
             """)
st.write("\n```\nε\n```\n")