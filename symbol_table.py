class SymbolTable:
    def __init__(self,length):
        self.size=length
        self.table={}

    def getHashKey(self,name:str):
        name=list(name)
        number=sum([ord(alphabet) for alphabet in name])
        return number%self.size
    
    def search(self,name:str):
        key=self.getHashKey(name)
        if key in self.table:
            for index,datas in enumerate(self.table[key]):
                if datas[index]==name:
                   return (key,index)
            return (key,-1)

        else:
            return (None,-1)
        
        
    def insert(self,
               name:str,
               type:str,
               size:int,
               dimension:int,
               line_of_code:int,
               address:str
               ):
        
        attributes=(name,type,size,dimension,line_of_code,address)
        key,index=self.search(name)
        
        if key and index+1:
            if self.table[key][index][0]==name:
                return None
            else:
                self.table[key].append(attributes)
        elif key and not index+1:
            self.table[key].append(attributes)
        else:
            key=self.getHashKey(name)
            self.table[key]=[]
            self.table[key].append(attributes)


    
        
    

    def update(self,
               name:str,
               type:str,
               size:int,
               dimension:int,
               line_of_code:int,
               address:str
            ):
        
        key,index=self.search(name)
        attributes=(name,type,size,dimension,line_of_code,address)
        if key and index+1:
            self.table[key][index]=attributes
        elif key and not index+1:
            self.table[key].append(attributes)
        else:
            self.table[key]=[]
            self.table[key].append(attributes)

    def delete(self,name:str):
        key,index=self.search(name)
        if key and index+1:
            deleted_data=self.table[key][index]
            del(self.table[key][index])
            return deleted_data
        else:
            return None

    
    
    def print_hash_table(self):
        print("------------------")
        for key,datas in self.table.items():
            chain=[]
            for data in datas:
                chain.append(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}")
            print(f"{key}->{chain}")
        print("-------------------")


if __name__=='__main__':
    symbolTable=SymbolTable(10)
    symbolTable.insert(
        "X","int",10,1,10,"0x2345"
    )
    symbolTable.insert(
        "Y","int",10,1,10,"0x2345"
    )
    symbolTable.insert(
        "Z","int",10,1,10,"0x2345"
    )
    symbolTable.print_hash_table()
    symbolTable.insert(
        "Y","int",11,1,10,"0x2345"
    )
    symbolTable.print_hash_table()

    symbolTable.update("Y","int",12,1,10,"0x2321")
    symbolTable.print_hash_table()  
    symbolTable.delete("X")
    symbolTable.print_hash_table()

    print(symbolTable.search("Z"))

    symbolTable.print_hash_table()

    symbolTable.insert("c","int",2,3,5,"0x2345")

    symbolTable.print_hash_table()
