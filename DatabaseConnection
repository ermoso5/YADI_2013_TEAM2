import psycopg2 as dbapi2
import sys
from sqlalchemy import *
from sqlalchemy.engine import reflection
from MainPKG.Basic_Classes import *
 
class Database:
    #engine = create_engine('postgresql://postgres:'+"a111111b"+'@localhost:5432/' +"TinyTwitter"+'') 
    #DB_name="TinyTwitter"
    #DB_user="postgres"
    #DB_password="a111111b"
    DB_name=""
    DB_user=""
    DB_password=""
    Map = Maps()
    engine=null
    Alchemy_engine=null
    def loadMap(self):
        try:
            self.engine = dbapi2.connect (database=self.DB_name, user=self.DB_user, password=self.DB_password)
            self.Alchemy_engine = create_engine('postgresql://postgres:'+self.DB_password+'@localhost:5432/'+self.DB_name+'') # I create a database named Datalog and the code is dmkm in postgreSQL
        except Exception as inst:
            print("Problem during create database engine")
            return
        self.Map=Maps()
        Inspector = reflection.Inspector.from_engine(self.Alchemy_engine)
        self.Alchemy_engine.echo = False 
        metadata = MetaData(self.Alchemy_engine)
        metadata.reflect(self.Alchemy_engine)    
        tables = metadata.tables.keys()
        for tableX in tables:
            Columns_list_temp=[]
            Columns_list=Inspector.get_columns(tableX,schema=None)
            for ColumnsX in Columns_list:
                Columns_list_temp.append(ColumnsX['name'])
            tableN=table(tableX,Columns_list_temp)
            self.Map.tables.append(tableN)
    
    def Select(self,Query):
        cur = self.engine.cursor()
        cur.execute (Query)
        return cur.fetchall()

class initialization_class:
    DB=null
    def intiatlize_console(self):
        self.DB=Database()
        print("Please enter the database name : ")
        database_name=sys.stdin.readline()
        database_name=database_name[:-1]
        #print(database_name)
        print("Please enter the database user name : ")
        database_username=sys.stdin.readline()
        database_username=database_username[:-1]
        #print(database_username)
        print("Please enter the database password : ")
        database_password=sys.stdin.readline()
        database_password=database_password[:-1]
        #print(database_password)
        self.DB.DB_name=database_name
        self.DB.DB_user=database_username
        self.DB.DB_password=database_password
        self.DB.loadMap()
        print("***  schema initialized successfully")
        
    DB_name=""
    DB_user=""    
    DB_password=""
        
    def Connet(self):
        self.DB=Database()
        self.DB.DB_name=self.DB_name
        self.DB.DB_user=self.DB_user
        self.DB.DB_password=self.DB_password
        self.DB.loadMap()
    
    
    def intiatlize_GUI(self):
        self.DB=Database()
        self.DB.DB_name=""
        self.DB.DB_user=""
        self.DB.DB_password=""
        self.DB.loadMap()
