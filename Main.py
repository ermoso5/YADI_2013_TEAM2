import psycopg2 as dbapi2
from sqlalchemy import *
from sqlalchemy.engine import reflection
import sys
from pyparsing import *
from MainPKG.Parser import *
from MainPKG.Evaluator import *
from MainPKG.DatabaseConnection import *




initClass=initialization_class()
initClass.intiatlize_console()
#initClass.DB_name="Datalog"
#initClass.DB_user="postgres"
#initClass.DB_password="a111111b"
#initClass.path = "C:\\Users\\qutiba\\Desktop\\Rule1.txt"
initClass.Connet()
DatalogParser1= DatalogParser(initClass.path)
#initClass.Query="reach(A,'G')"
EC=Evalutor(DatalogParser1,initClass)
while true:
    print("Please enter the qurey : ")
    initClass.Query=sys.stdin.readline()
    initClass.Query=initClass.Query[:-1]
    if initClass.Query == "-1":
        sys.exit()
    
    EC.PrepareRules_create_views_for_primary_rules()
    EC.Execute(initClass.Query)
    #     student_book_age(A,D,R)    
        
    
    
    
    
