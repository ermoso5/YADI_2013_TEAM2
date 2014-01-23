import psycopg2 as dbapi2
from sqlalchemy import *
from sqlalchemy.engine import reflection
import sys
from pyparsing import *
from MainPKG.Parser import *
from MainPKG.Evaluator import *
from MainPKG.DatabaseConnection import *
#===============================================================================
#
# initClass=initialization_class()
# initClass.intiatlize_console()
# #print("Please enter the Rule file path : ")
# #path=sys.stdin.readline()
# path = 'C:/Python33/Rules.txt' #path[:-1]
#
# DatalogParser1= DatalogParser(path)
#
# Rs=DatalogParser1.GetRules()
# EC=Evalute()
# query="aV(X,Y)"
# F=DatalogParser1.toPredicate(Grammar().literal.parseString(query))
#===============================================================================

#===============================================================================
# #initClass.DB_name="Datalog"
# #initClass.DB_user="postgres"
# #initClass.DB_password="a111111b"
# #initClass.Connet()
# #@"C:\\Users\\qutiba\\Desktop\\Rules.txt"
#
# for R in Rs:
#     if R.Head.Name==F.Name:
#         EC.evalute(R)
#         print()
#         print("Query is ")
#         print(EC.sql_tables+" where "+EC.sql_condition)
#         break
#
# DB=Database()
#
# print()
# print()
#
# Rows=initClass.DB.Select(EC.sql_tables+" where "+EC.sql_condition)
# for R in Rows:
#     print(R)
#===============================================================================



######QUTIBA'S TEST

initClass=initialization_class()
#initClass.intiatlize_console()


initClass.DB_name="Datalog"
initClass.DB_user="postgres"
initClass.DB_password="_password"
initClass.Connet()
path = "C:/Python33/Rules.txt"
DatalogParser1= DatalogParser(path)

query="student_book_age(S,F,20)"
#try:
EC=Evalutor(DatalogParser1,initClass)
#query="student_book(D,V)"
EC.Execute(query)

print("4")

for r in EC.Rules:
    print(r.View_name)
    print("----------- "+str(r.IsRecusive))


