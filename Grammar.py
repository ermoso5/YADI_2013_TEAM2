from pyparsing import *

class Grammar:
    def __init__(self):
        operator = oneOf("+ - * / % ^")
        built_operations = ['=', '!=', '>=', '<=', '>', '<', 'is']
        capital_words = Combine(Word("ABCDEFGHIJKLMNOPQRSTUVWXYZ_", exact=1) + Optional(Word(alphanums)))# define predicate names starting with capital letters
        small_words = Combine(Word("abcdefghijklmnopqrstuvwxyz") + Optional(Word(alphanums+"_")))
        string = QuotedString(quoteChar="'",unquoteResults=False)
        number = Combine(Optional(oneOf("- +")) + Word(nums) + Optional(Literal('.') + OneOrMore(Word(nums)) + Optional(Literal("E") + OneOrMore(Word(nums)) ))) #+StringEnd())

        predicate_name = small_words
        variable = Literal('_') | capital_words
        constant = number | small_words | string

        term = variable | constant
        term_list = delimitedList(term, delim=',').setName("paramList")
        fact_arg_list = delimitedList(constant, delim=',').setName("factParamList")
        pos_literal = predicate_name + Literal("(").suppress() + term_list + Literal(")").suppress()
        neg_literal = Literal("not") +Literal("(").suppress() + pos_literal + Literal(")").suppress()
        literal = pos_literal | neg_literal #+ expression

        head = pos_literal

        fact = predicate_name + Literal("(").suppress() + fact_arg_list + Literal(")").suppress() + Literal(".").suppress() + StringEnd()

        built = Group(term + ZeroOrMore(operator + term)) + oneOf(built_operations) + Group(term + ZeroOrMore(operator + term))
        self.expression = expression = built

        body = delimitedList(Group(literal | expression),delim=',' ).setName("predicateList") +Literal(".").suppress() + StringEnd()
        self.rule = (Group(head) + ":-" + Group(body))
        self.no_body_rule = Group(head) + Literal(".").suppress() + StringEnd()
        self.literal = literal
        self.constant = constant
        self.built_operations = built_operations
        self.fact = fact

