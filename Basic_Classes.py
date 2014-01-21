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
    def __init__(self):
        self.Name = ""
        self.Slots = []
        self.IsNegation = False
    def print(self):
        print(self.Name+'(', end="")
        for p in self.Slots:
            print(p.Value + ',' + p.VariableName, end="")
        print(')', end="")

class Rule:
    def _init__(self):
        self.Head = Predicate()
        self.Body = []
    def print(self):
        print("Head:", end="")
        if self.Head is not None:
            self.Head.print()
        print("Body:", end="")
        for i in range(0,len(self.Body), 1):
            self.Body[i].print()


class Expression:
    def __init__(self):
        self.Literals = []
    def print(self):
    #[['X'], '>=', ['2', '+', 'Y']]
        print(self.Literals)

class Maps:
    tables=[]

class table:
    def __init__(self, name1, Arrenged_Columns):
        self.name=name1
        self.Arrenged_Columns=Arrenged_Columns

class perdicate_variable:
    def __init__(self):
        self.Var_name=""
        self.table_alias = ""

