from pyparsing import *

class DatalogParser:
    def __init__(self, input):
        self.datalogString = input # V(X,Y) :- R(X,Z), Q(x,'20').?- V(X,Y).

    def getStatements(self):
        return self.datalogString.split(".") #rules and query
        
    def GetQuery(self):
        statements = self.getStatements() #rules and query
        statement_number = len(statements)
        try:
            query = statements[statement_number - 2]
        except IndexError:
            print("Input is not valid")
            return
        
        query_rule = Literal("?-").suppress() + Grammar().predicateRule()
        try:
            query_breakdown = query_rule.parseString(query)
        except ParseException:
            print("No query specified")
            return
        return self.toPredicate(query_breakdown)
        
    def GetRules(self):
        #program_rule = OneOrMore(Word(printables) + Literal(".").suppress()) + StringEnd()
        #statements = program_rule.parseString(self.datalogString)
        rules = []
        statements = self.getStatements() #rules and query
        statement_number = len(statements)

        try:
            for i in range(0, statement_number-2, 1):
                new_rule = self.toRule(statements[i])
                rules.append(new_rule)
        except ParseException:
            print("The rules were not valid.")
        return rules
        
    def toPredicate(self, input_break):
        #input_break - [Name, [P1, P2, ..., PN]]
        predicate = Predicate()
        predicate.Name = input_break[0]
        predicate.Slots = []
        
        for i in range(1, len(input_break), 1):
            slot = Slot(input_break[i])
            predicate.Slots.append(slot)  
        return predicate

    def toRule(self, input):
        statement_breakdown = Grammar().statementRule().parseString(input)
        if not statement_breakdown[1] == ":-":
            print("Something went wrong")
            return
        
        rule = Rule()
        rule.Head = self.toPredicate(statement_breakdown[0])
        rule.Body = []
        for i in range(0, len(statement_breakdown[2]), 1):
            rule.Body.append(self.toPredicate(statement_breakdown[2][i]))
        
        return rule
            
    def Print(self):
        for i in self.GetRules():
            print()
            i.print()
        
    
class Slot:
    def __init__(self, arg):
        self.VariableName = self.Value = ""
        try:
            dummy = Grammar().constantRule().parseString(arg)
            self.Value = arg
        except ParseException:          
            self.VariableName = arg
    def print(self):
        print(self.Value + self.VariableName, end="")

class Predicate:
    def __init__(self):
        self.Name = ""
        self.Slots = []
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
        self.Head.print()
        print("Body:", end="")
        for i in range(0,len(self.Body), 1):
            self.Body[i].print()
            
class Grammar:
        def __init__(self):
            operator = Word("+-*/=<><=>=!=")
            capital_words = Combine(Word("ABCDEFGHIJKLMNOPQRSTUVWXYZ_") + Optional(Word(alphanums))) # define predicate names starting with capital letters
            small_words = Combine(Word("abcdefghijklmnopqrstuvwxyz") + Optional(Word(alphanums+"_")))
            string = QuotedString(quoteChar="'",unquoteResults=False) 
            number = Combine(Optional(Word("-")) + Word(nums) + Optional(Literal('.') + OneOrMore(Word(nums)) + Optional(Literal("E") + OneOrMore(Word(nums)) ))) #+StringEnd())
                     
            predicate_name = capital_words  
            variable = Literal('_') | capital_words
            constant = number | small_words | string

            param = variable | constant
            param_list = delimitedList(Optional(quotedString.copy() | param, default=""),delim=',' ).setName("paramList")
            predicate_rule =  predicate_name + Literal("(").suppress() + param_list + Literal(")").suppress()
                    
            head_param_list = delimitedList(Optional(quotedString.copy() | variable, default=""),delim=',' ).setName("paramList")
            head_rule = predicate_name + Literal("(").suppress() + head_param_list + Literal(")").suppress()

            predicate_list = delimitedList(Optional(quotedString.copy() | Group(predicate_rule), default=""),delim=',' ).setName("predicateList")
            self.statement_rule = Group(head_rule) + ":-" + Group(predicate_list)
            self.predicate_rule = predicate_rule
            self.constant_rule = constant
        def statementRule(self):
            return self.statement_rule
        
        def predicateRule(self):
            return self.predicate_rule

        def constantRule(self):
            return self.constant_rule

    


    
