from pyparsing import *
from MainPKG.Basic_Classes import *

class DatalogParser:
    def __init__(self, input_file):
        self.rules_file = input_file
        self.log_file = 'C:/Python33/YADI_log.txt'
        open(self.log_file, 'w').close()

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
                new_rule = self.toRule(i)
            except Exception:
                open(self.log_file, 'a').write("Found an error in rule number "+ str(rule_number)).close()
                return

            if not self.checkSafety(new_rule):
                open(self.log_file, 'a').write("Warning: Rule number "+ str(rule_number) + " is not safe.").close()
            rules.append(new_rule)
            rule_number += 1
        return rules

    def GetRuleFromQuery(self, query):
        rules = self.GetRules()
        query = self.toPredicate(Grammar().no_body_rule.parseString(query))
        query_rule_found = False
        for r in rules:
            if query.Name == r.Head.Name:
                if len(query.Slots) == len(r.Head.Slots):
                    return query
                else:
                    query_rule_found == False
        if not query_rule_found:
            log = open(self.log_file, 'a')
            log.write('There is no rule defining the predicate of the query.')
            log.close()

    def Print(self):
        for i in self.GetRules():
            print()
            i.print()

    ############# PRIVATE FUNCTIONS #####################

    def getStatements(self):
        return filter(None, open(self.rules_file).read().splitlines())

    def checkSafety(self, rule):
        #rule = self.toRule(rule)
        isSafe = True
        head_var = rule.Head.Slots
        pos_var = []
        #get all variables in positive goals
        for g in rule.Body:
            if type(g) == Predicate:
                if not g.IsNegation:
                    for s in g.Slots:
                        if s.VariableName:
                            pos_var.append(s.VariableName)

        for h in rule.Head.Slots:
            if h.VariableName:
                if not h.VariableName in pos_var:
                     isSafe = False

        for b in rule.Body:
            if type(b) == Expression:
                for a in self.varFromExpr(b):
                    if not a in pos_var:
                        isSafe = False

        for g in rule.Body:
            if type(g) == Predicate:
                if g.IsNegation:
                    for s in g.Slots:
                        if s.VariableName and not s.VariableName in pos_var:
                            isSafe = False

        return isSafe

    def varFromExpr(self, expr):
        all = expr.Literals[0]+expr.Literals[2]
        vars = []
        for a in all:
            try:
                Grammar().variable.parseString(a)
                vars.append(a)
            except Exception:
                continue
        return vars

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
        try:
            statement_breakdown = Grammar().rule.parseString(input)
        except ParseException:
            try:
                statement_breakdown = Grammar().no_body_rule.parseString(input)
            except ParseException:
                open(self.log_file, 'a').write('The rule was not valid.').close()

        rule = Rule()
        rule.Head = self.toPredicate(statement_breakdown[0])
        rule.Body = []

        if len(statement_breakdown) > 1:
            body = statement_breakdown[2]

            for i in range(0, len(body), 1):
                try:
                    rule.Body.append(self.toGoal(body[i]))
                except Exception:
                    print("Error on parsing")
        return rule

    def toFact(self, input):
        input_break = Grammar().fact.parseString(input)
        fact = Fact()
        fact.Name = input_break[0]

        print(input_break)

        fact.Slots = []

        for i in range(1, len(input_break), 1):
            slot = Slot(input_break[i])
            fact.Slots.append(slot)

        return fact



