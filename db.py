import psycopg2 as dbapi2
from sqlalchemy import *

class Predicate:
    alias=""
    def __init__(self, name, slots):
        self.Name=name
        self.Slots = slots
        
class slot:
    def __init__(self, Value , variableName):
        self.Value=Value ## in case of constant fill value here
        self.variableName = variableName ## in case of variable put the name here

class perdicate_variable:
    def __init__(self):
        self.Var_name=""
        self.table_alias = ""
    
class Rule:
    def __init__(self, head1, body1):
        self.head=head1 # it will be predicate
        self.body=body1 # it will be list of predicates
###################################################################
        
class Maps:
     tables=[]
     
class table:
   def __init__(self, name1, Arrenged_Columns):
       self.name=name1
       self.Arrenged_Columns=Arrenged_Columns
       
class operation:
    def get_Column_name(self,tableName,index):
        for i in Maps.tables:
            i.__class__=table
            if i.name == tableName:
                return i.Arrenged_Columns[index]




class Database:
    
    engine = dbapi2.connect (database="datalog", user="postgres", password="dmkm")
    def createTable(self,Pred):
        cur =self.engine.cursor()
        que="create table "
        que+= Pred.Name
        que+="("
        c=0
        for slotI in Pred.Slots:
            que+= "col"+c.__str__() +" varchar ,"
            c+=1
        que=que[:-1] ## remove the last comma
        que +=",id serial PRIMARY KEY)"
        print(que)
        cur.execute (que)
        self.engine.commit()
      
    def insertRow(self,Pred):
        cur = self.engine.cursor()       
        quer="INSERT INTO "
        opera1=operation()
        col=""
        ii=0
        quer+=Pred.Name
        quer+=" VALUES ("
        quer +="'"
        c=0
        for k in Pred.Slots:
            quer +=Pred.Slots[c].Value
            c+=1
            quer +="','"
        quer =quer[:-2]
        quer +=") "
        cur.execute (quer)
        self.engine.commit()
        
        
        
        
 
Pred=Predicate("Fact12",[slot("ABC",""),slot("123",""),slot("555","") ])        
               
                
Map = Maps()
Map.tables.append(table("T",["col1","col2","col7"])) ## generate headers
Map.tables.append(table("r",["col3","col4"]))
Map.tables.append(table("s",["col5","col6"]))

operation1=operation()
                
print(operation1.get_Column_name("T",2))  

DB=Database()

DB.createTable(Pred)
DB.insertRow(Pred)  

