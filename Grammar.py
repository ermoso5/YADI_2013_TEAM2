from pyparsing import *

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
        param_list = delimitedList(param,delim=',' ).setName("paramList")
        pos_predicate_rule = predicate_name + Literal("(").suppress() + param_list + Literal(")").suppress()
        neg_predicate_rule = Literal("not") +Literal("(").suppress() + pos_predicate_rule + Literal(")").suppress()
        predicate_rule = pos_predicate_rule | neg_predicate_rule

        head_param_list = delimitedList(variable, delim=',' ).setName("paramList")
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
