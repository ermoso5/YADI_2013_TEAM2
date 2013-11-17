from pyparsing import *

class DatalogParser:
    def __init__(self, input_file):
        self.rules_file = input_file 

    ##############  API ########################

    def SetQuery(self, query):
        self.query = query
        
    def GetQuery(self):      
        query_rule = Literal("?-").suppress() + Grammar().predicateRule()
        try:
            query_breakdown = query_rule.parseString(self.query)
        except ParseException:
            print("No query specified")
            return
        
        return self.toPredicate(query_breakdown)
        
    def GetRules(self):
        rules = []
        rule_number = 1
        
        for i in self.getStatements():
            try:
                Grammar().factRule().parseString(i)
                new_rule = self.toFact(i)
            except ParseException:
                try:
                    new_rule = self.toRule(i)
                except ParseException:
                    print("Found an error in rule "+ str(rule_number))
                    return
            rules.append(new_rule)
            rule_number += 1
        return rules

    def Print(self):
        for i in self.GetRules():
            print()
            i.print()

    ############# PRIVATE FUNCTIONS #####################

    def getStatements(self):
        return open(self.rules_file).read().splitlines()
        
    def toPredicate(self, input_break):
        #input_break - [Opt(not), Name, P1, P2, ..., PN]
        predicate = Predicate()
        if input_break[0] == 'not':
            param_index = 2
            predicate.IsNegation = True
            predicate.Name = input_break[1]
        else:
            param_index = 1
            predicate.Name = input_break[0]
        predicate.Slots = []
        
        for i in range(param_index, len(input_break), 1):
            slot = Slot(input_break[i])
            predicate.Slots.append(slot)  
        return predicate

    def toExpression(self, input_break):
        expr = Expression()
        expr.Literals = input_break
        return expr
    
    def toGoal(self, input_break):
        if '=' in list(input_break):
            return self.toExpression(input_break)
        else:
            return self.toPredicate(input_break)            
            
    
    def toRule(self, input):
        statement_breakdown = Grammar().statementRule().parseString(input)
        if not statement_breakdown[1] == ":-":
            print("Something went wrong")
            return
        
        rule = Rule()
        rule.Head = self.toPredicate(statement_breakdown[0])
        rule.Body = []
        for i in range(0, len(statement_breakdown[2]), 1):
            rule.Body.append(self.toGoal(statement_breakdown[2][i]))
        
        return rule
    
    def toFact(self, input):
        input_break = Grammar().factRule().parseString(input)
        fact = Predicate()
        print(input_break)
        if input_break[0] == 'not':
            param_index = 2
            fact.IsNegation = True
            fact.Name = input_break[1]
        else:
            param_index = 1
            fact.Name = input_break[0]
        fact.Slots = []
        
        for i in range(param_index, len(input_break), 1):
            slot = Slot(input_break[i])
            fact.Slots.append(slot)  
        return fact
    
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
        self.IsNegation = False
    def print(self):
        print(self.Name+'(', end="")
        for p in self.Slots:
            print(p.Value + ',' + p.VariableName, end="")
        print(')', end="")

class Expression:
    def __init__(self):
        self.Literals = []

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
                     
            predicate_name = small_words  
            variable = Literal('_') | capital_words
            constant = number | small_words | string

            param = variable | constant
            param_list = delimitedList(Optional(quotedString.copy() | param, default=""),delim=',' ).setName("paramList")
            pos_predicate_rule = predicate_name + Literal("(").suppress() + param_list + Literal(")").suppress()
            neg_predicate_rule = Literal("not") +Literal("(").suppress() + pos_predicate_rule + Literal(")").suppress()
            predicate_rule = pos_predicate_rule | neg_predicate_rule
            
            head_param_list = delimitedList(Optional(quotedString.copy() | variable, default=""),delim=',' ).setName("paramList")
            pos_head_rule = predicate_name + Literal("(").suppress() + head_param_list + Literal(")").suppress()
            neg_head_rule = Literal("not") + Literal("(").suppress() + pos_head_rule + Literal(")").suppress()
            head_rule = pos_head_rule | neg_head_rule

            fact_rule = predicate_rule + Literal(".").suppress() + StringEnd()
    
            self.equation = equation = param + Literal("=") + param
                        
            predicate_list = delimitedList(Optional(quotedString.copy() | Group(predicate_rule | equation), default=""),delim=',' ).setName("predicateList")
            self.statement_rule = (Group(head_rule) + ":-" + Group(predicate_list)) | fact_rule
            self.predicate_rule = predicate_rule
            self.constant_rule = constant
            self.fact_rule = fact_rule
            
        def statementRule(self):
            return self.statement_rule

        def factRule(self):
            return self.fact_rule
        
        def predicateRule(self):
            return self.predicate_rule

        def constantRule(self):
            return self.constant_rule

        def equationRule(self):
            return self.equation

    


    
