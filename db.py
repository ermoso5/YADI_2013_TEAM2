'''
Created on 16 nov. 2013

@author: hussein
'''
import psycopg2 as dbapi2
db = dbapi2.connect (database="datalog", user="postgres", password="dmkm")
cur = db.cursor()

class Predicate:
    alias=""
    def __init__(self, name, slots):
        self.Name=name
        self.Slots = slots  
        
class slot:
    def __init__(self, Value , variableName):
        self.Value=Value                              ## in case of constant fill value here 
        self.variableName = variableName              ## in case of variable put the name here
         
Pred=Predicate("Fact1",[slot("ABC",""),slot("123",""),slot("555","") ])

class Database:
    def createTable(self,Pred):
        str="create table ("
        str+= Pred.name
        c=0
        for i in Pred.slot:
            str+= "col"+c.__str__+"  varchar ,"
            c+=1
        str=str[:-1]   ## remove the last comma    
        str +=",id serial PRIMARY KEY)"
        ##print(str)
        cur.execute (str)
        db.commit()
        str1 ="INSERT INTO "
        str1+= Pred.name
        c=0
        srt1 +="("
        for j in Pred.slot:
            st1r += "col"+c.__str__
            c+=1
        str1 +=") VALUES ("
        c=0
        for k in Pred.slot:
            str1 +=Pred.slot(c).Value
            c+=1
        str1 +="))"
        cur.execute (str1)
        db.commit()
       
