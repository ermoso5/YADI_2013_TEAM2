class Predicate:
    alias=""
    def __init__(self, name, slots):
        self.Name=name
        self.Slots = slots  
        
class slot:
    def __init__(self, Value , variableName):
        self.Value=Value                              ## in case of constant fill value here 
        self.variableName = variableName              ## in case of variable put the name here
         

class Database:
    def createTable(self,Pred):
      re=1
      ## 1- check for existance
	  
      ## 2- if not exists create table
      ## 3- insert slots value as the arrangement order (get the slot.Value not slot.variableName )
    
        
P=Predicate("Fact1",[slot("ABC",""),slot("123",""),slot("555","") ])
