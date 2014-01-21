from pyparsing import *
from MainPKG.Basic_Classes import *

class DatalogParser:
    def __init__(self, input_file):
        self.rules_file = input_file
        open('C:/Python33/YADI_log.txt', 'w').close()

    ##############  API ########################

    def SetQuery(self, query):
        self.query = query

    def GetQuery(self):
        query_rule = Literal("?-").suppress() + Grammar().literal
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
            i= i.strip()
            try:
                Grammar().fact.parseString(i)
                new_rule = self.toFact(i)
            except Exception:
                try:
                    new_rule = self.toRule(i)
                except ParseException:
                    print("Found an error in rule number "+ str(rule_number))
                    return
            rules.append(new_rule)
            rule_number += 1
        return rules

    def GetRuleFromQuery(self, query):
        rules = self.GetRules()
        query = self.toPredicate(Grammar().fact.parseString(query))
        query_rule_found = False
        for r in rules:
            if query.Name == r.Head.Name:
                if len(query.Slots) == len(r.Head.Slots):
                    return query
                else:
                    query_rule_found == False
        if not query_rule_found:
            log = open('C:/Python33/YADI_log.txt', 'w')
            log.write('There is no rule defining the predicate of the query.')
            log.close()

    def Print(self):
        for i in self.GetRules():
            print()
            i.print()

    ############# PRIVATE FUNCTIONS #####################

    def getStatements(self):
        return filter(None, open(self.rules_file).read().splitlines())

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
        #input_break - [Opt(not), Name, P1, P2, ..., PN]
        if input_break[1] in Grammar().built_operations:
            return self.toExpression(input_break)
        else:
            return self.toPredicate(input_break)


    def toRule(self, input):
        statement_breakdown = Grammar().rule.parseString(input)

        if not statement_breakdown[1] == ":-":
            print("Something went wrong")
            return

        rule = Rule()
        rule.Head = self.toPredicate(statement_breakdown[0])
        rule.Body = []
        body = statement_breakdown[2]

        for i in range(0, len(body), 1):
            try:
                rule.Body.append(self.toGoal(body[i]))
            except Exception:
                print("Error on parsing")
        return rule

    def toFact(self, input):
        input_break = Grammar().fact.parseString(input)
        fact = Predicate()
        rule = Rule()
        rule.Head = None
        rule.Body = []

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
        rule.Body.append(fact)
        return rule



