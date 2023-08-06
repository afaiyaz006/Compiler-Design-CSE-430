class SymbolTable:
    def __init__(self,length):
        self.size=length
        self.table={}

    def getHashKey(self,name:str)->int:
        
        name=list(name)
        number=sum([ord(alphabet) for alphabet in name])
        return number%self.size
    
    def search(self,name:str)->tuple:
       
        key=self.getHashKey(name)
        if key in self.table:
            for index,datas in enumerate(self.table[key]):
                if datas[0]==name:
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
               )->tuple:
        
        attributes=(name,type,size,dimension,line_of_code,address)
        key,index=self.search(name)
        
        if key and index+1:
            if self.table[key][index][0]==name:
                return None
            else:
                self.table[key].append(attributes)
                return attributes
        elif key and not index+1:
            self.table[key].append(attributes)
            return attributes
        else:
            key=self.getHashKey(name)
            self.table[key]=[]
            self.table[key].append(attributes)
            return attributes

    
        
    

    def update(self,
               name:str,
               type:str,
               size:int,
               dimension:int,
               line_of_code:int,
               address:str
            )->tuple:
        
        key,index=self.search(name)
        attributes=(name,type,size,dimension,line_of_code,address)
        if key and index+1:
            self.table[key][index]=attributes
            return attributes
        elif key and not index+1:
            self.table[key].append(attributes)
            return attributes
        else:
            self.table[key]=[]
            self.table[key].append(attributes)
            return attributes
        
    def delete(self,name:str)->tuple:
        key,index=self.search(name)
        
        if key and index+1:
            deleted_data=self.table[key][index]
            del(self.table[key][index])
            return deleted_data
        else:
            return None

    
    
    def print_hash_table(self)->None:

        print("------------------")
        for key,datas in self.table.items():
            chain=[]
            for data in datas:
                chain.append(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}")
            print(f"{key}->{chain}")
        print("-------------------")


def demo():
    symboltable=SymbolTable(10)
    f = open("symbol_table_input.txt", "r")
    datas=f.read()
    f.close()
    datas=datas.split("\n")[1:]
   
    for data in datas:
        data=data.split(",")
        operation=data[0]
        
        if operation=="add":
            ops,name,type_,size_,dim,loc,address=data[0],data[1],data[2],int(data[3]),int(data[4]),int(data[5]),data[6]
            print(f"Inserted: {symboltable.insert(name,type_,size_,dim,loc,address)}")
            symboltable.print_hash_table()
        
        elif operation=="update":
            ops,name,type_,size_,dim,loc,address=data[0],data[1],data[2],int(data[3]),int(data[4]),int(data[5]),data[6]
            print(f"Updated {symboltable.update(name,type_,size_,dim,loc,address)}")
            symboltable.print_hash_table()

        elif operation=="del":
            ops,name=data[0],data[1]
            print(f"Deleted Data: {symboltable.delete(name)}")
            symboltable.print_hash_table()

        elif operation=="search":
            ops,name=data[0],data[1]
            print(ops,name)
            print(f"Found data at: {symboltable.search(name)}")
            symboltable.print_hash_table()

if __name__=='__main__':
    demo()