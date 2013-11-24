from pyparsing import *

class Grammar:
    def __init__(self):
        operator = Word("+-*/=<><=>=!=")
        capital_words = Combine(Word("ABCDEFGHIJKLMNOPQRSTUVWXYZ_", exact=1) + Optional(Word(alphanums)))# define predicate names starting with capital letters
        small_words = Combine(Word("abcdefghijklmnopqrstuvwxyz") + Optional(Word(alphanums+"_")))
        string = QuotedString(quoteChar="'",unquoteResults=False)
        number = Combine(Optional(oneOf("- +")) + Word(nums) + Optional(Literal('.') + OneOrMore(Word(nums)) + Optional(Literal("E") + OneOrMore(Word(nums)) ))) #+StringEnd())

        predicate_name = small_words
        variable = Literal('_') | capital_words
        constant = number | small_words | string

        term = variable | constant
        term_list = delimitedList(term, delim=',').setName("paramList")
        pos_literal = predicate_name + Literal("(").suppress() + term_list + Literal(")").suppress()
        neg_literal = Literal("not") +Literal("(").suppress() + pos_literal + Literal(")").suppress()
        literal = pos_literal | neg_literal #+ expression

        head = pos_literal

        fact = literal + Literal(".").suppress() + StringEnd()

        self.equation = equation = term + Literal("=") + term

        body = delimitedList(Group(literal | equation),delim=',' ).setName("predicateList")
        self.rule = (Group(head) + ":-" + Group(body)) | fact
        self.literal = literal
        self.constant = constant
        self.fact = fact

