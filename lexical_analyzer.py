#lexical analyzer
#author:A.Faiyaz
import re
from collections import OrderedDict
key_words=[
        "auto",
        "break",
        "case",
        "char", 
        "const", 
        "continue",
        "default",
        "do",
        "double",
        "else", 
        "enum", 
        "extern",
        "float", 
        "for", 
        "goto", 
        "if",
        "int",
        "long",
        "register",
        "return",
        "short",
        "signed",
        "sizeof",
        "static",
        "struct",
        "switch", 
        "typedef", 
        "union",
        "unsigned",
        "void", 
        "volatile",
        "while"
]
def remove_dups(datas:list)->list:
    """
        Removes duplicates from list but keep the order preserverd.
    """
    return list(OrderedDict.fromkeys(datas))

def lexical_analyzer(program:str)->dict[str:list[str]]:
    """
        A simple lexical analyzer function
        :input:
            program:
            A program in c.

        :output:
            dictionary containing tokens of various types.
            "keywords":keywords,
            "identifiers":identifiers,
            "arithmatic_operators":arithmatic_operators,
            "constants":constants,
            "punctuations_signs":punctuations_signs,
            "logical_operators":logical_operators,
            "parenthesis":parenthesis,
            
    """

    # for removing any kind of comments
    comment_pattern=r"//.*\n"
    program=re.split(comment_pattern,program)
    program="".join(program)


    #for finding token types
    identifiers=re.findall("[a-zA-Z]+[0-9]|[a-zA-Z]+",program)
    constants=re.findall("[0-9]+",program)
    punctuations_signs=re.findall("[;]|[-]|[,]",program)
    arithmatic_operators=re.findall("[+]|[-]|[*]|[=]|[/]",program)
    logical_operators=re.findall("[>]|>=|<|<=|==|!=",program)
    parenthesis=re.findall("[{]|[}]|[(]|[)]|[{]|[}]",program)
    keywords=re.findall("|".join(key_words),program)
    
    #removing duplicates
    identifiers=remove_dups(identifiers)
    punctuations_signs=remove_dups(punctuations_signs)
    arithmatic_operators=remove_dups(arithmatic_operators)
    logical_operators=remove_dups(logical_operators)
    keywords=remove_dups(keywords)

    #removing keyword which were identified as identifier
    #regex likhar iccha chilo but parlam na
    for key_word in keywords:
        if key_word in identifiers:
            identifiers.remove(key_word)
    

    return {
        "keywords":keywords,
        "identifiers":identifiers,
        "arithmatic_operators":arithmatic_operators,
        "constants":constants,
        "punctuations_signs":punctuations_signs,
        "arithmatic_operators":arithmatic_operators,
        "logical_operators":logical_operators,
        "parenthesis":parenthesis,
    }
    
if __name__=='__main__':
    program=""""""
    while True:
        try:
            line=input()
            if line=="EOF":
                break
            program+=line+"\n"
        except EOFError:
            break    

    lexemes=lexical_analyzer(program)

    print(f"Keywords({len(lexemes['keywords'])}): {' , '.join(lexemes['keywords'])}")
    print(f"Identifiers({len(lexemes['identifiers'])}): {' , '.join(lexemes['identifiers'])}")
    print(f"Constants({len(lexemes['constants'])}): {' , '.join(lexemes['constants'])}")
    print(f"Punctuations signs({len(lexemes['punctuations_signs'])}): {' , '.join(lexemes['punctuations_signs'])}")
    print(f"Arithmatic operators({len(lexemes['arithmatic_operators'])}): {' , '.join(lexemes['arithmatic_operators'])}")
    print(f"Logical operators({len(lexemes['logical_operators'])}): {' , '.join(lexemes['logical_operators'])}")
    print(f"Parenthesis({len(lexemes['parenthesis'])}): {' , '.join(lexemes['parenthesis'])}")
    
