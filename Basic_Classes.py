from MainPKG.Grammar import *
from pyparsing import ParseException

class Slot:
    def __init__(self, arg):
        self.VariableName = self.Value = ""
        try:
            dummy = Grammar().constant.parseString(arg)
            self.Value = arg
        except ParseException:
            self.VariableName = arg
    def print(self):
        print(self.Value + self.VariableName, end="")

class Predicate:
    Non_repeated_perdicate_variables=[]
    alias=""
    Slots = []
    def __init__(self):
        self.Name = ""
        self.Slots = []
        self.IsNegation = False
    def GetName(self):
        return self.Name
    def GetArity(self):
        return len(self.Slots)
    def print(self):
        print(self.Name+'(', end="")
        for p in self.Slots:
            print(p.Value + ',' + p.VariableName, end="")
        print(')', end="")

class Rule:
    IsPrimary=None     # means it has no body " R(X,Y,X). " or all body's predicates are tables in Database
    IsRecusive=None
    #parameters related to structure of rule query
    sql_condition=""
    sql_tables=" "
    View_query=""
    View_name=""
    #################

    #parameters related to unify the rules with query  ex  Q('AXCV',10)
    Where_clause=""
    #################
    Rec_view="" 
    
    def Print_result(self,DB):
        sql="select * from "+self.View_name
        if self.Where_clause !="":
            sql+=" where "+self.Where_clause 
        rows =DB.Select(sql)
        for row in rows :
            print (self.Head.Name+str(row))
          
    def  print2(self):
        R=self
        print("R.View_name "     + R.View_name)
        print("R.sql_condition " + R.sql_condition)
        print("R.sql_tables "    + R.sql_tables)
        print("R.View_query "    + R.View_query)
        print("R.Where_clause "  + R.Where_clause)
        print("R.get_Query "     + R.get_Query())
        
        for S in R.Body:
            print("       " + S.alias)
            print("_________________________")
            
            for E in S.Non_repeated_perdicate_variables:
                print("       "+E.Var_name+":" +E.table_alias)
            
            print("_________________________")
    

    def get_Query(self):
        if self.sql_condition=="":
            return self.sql_tables
        else:
            return self.sql_tables +" where "+self.sql_condition

    def _init__(self):
        self.Head = Predicate()
        self.Body = []
    def GetHeadName(self):
        return self.Head.GetName()
    def GetRuleArity(self):
        return len(self.Body)
    def print(self):
        print("Head:", end="")
        if self.Head is not None:
            self.Head.print()
        print("Body:", end="")
        for i in range(0,len(self.Body), 1):
            self.Body[i].print()

class Fact:
    def __init__(self):
        self.Name = ""
        self.Slots = []
    def GetName(self):
        return self.Name
    def GetFactArity(self):
        return len(self.Slots)
    def print(self):
        print(self.Name+'(', end="")
        for p in self.Slots:
            print(p.Value + ',' + p.VariableName, end="")
        print(')', end="")

class Expression:
    def __init__(self):
        self.Literals = []
    def GetOperation(self):
        return self.Literals[1]
    def print(self):
    #[['X'], '>=', ['2', '+', 'Y']]
        print(self.Literals)

class Maps:
    tables=[]
    views=[]

class table:
    def __init__(self, name1, Arrenged_Columns):
        self.name=name1
        self.Arrenged_Columns=Arrenged_Columns

class view:
    def __init__(self, name,alias, Arrenged_Columns):
        self.alias=alias
        self.name=name
        self.Arrenged_Columns=Arrenged_Columns




class perdicate_variable:
    def __init__(self):
        self.Var_name=""
        self.table_alias = ""


