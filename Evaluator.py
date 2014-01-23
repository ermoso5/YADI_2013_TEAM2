from MainPKG.Basic_Classes import *
from sqlalchemy.dialects.mssql.information_schema import views
from MainPKG.DatabaseConnection import *

class Evalutor:
    Final_query=""
    DatalogParserT=""
    initClass=""
    Rules=[]
    Views_list=[]
    Rules_to_be_executed=[]


    def __init__(self, DatalogParserT1,initClassT):

        self.DatalogParserT=DatalogParserT1

        self.initClass=initClassT

        self.Rules=DatalogParserT1.GetRules()

        self.PrepareRules_generate_View_alias_for_rule_header()               # for all rules generate alias for headers

        self.PrepareRules_generate_alias_for_predicate_by_its_tablename()     # for predicates in rules' bodies that represent tables in DB

        self.PrepareRules_check_primary_rules()                               # check if all predicates of the rule's body are tables

        self.PrepareRules_Body_slots_alias_names()                            # for primary predicate get the slot expression   for example if we have table with name tab and on column ID them the predicate tab(X) slot will be :  X is defined as tab_ins1.ID   where tab_ins1 is alias for tab table

        self.PrepareRules_Primary_get_Head_slots_relations_with_body()            # join the head slots with body slots r1(X,Y):-pred1(X,Z),pred2(Z,Y) the result in the head will be the first column of pred1 and second column in pred2

        self.PrepareRules_Primary_get_sql_queries()                           #

        self.PrepareRules_create_views_for_primary_rules()



    def Drop_created_views(self):
       for view in self.Views_list:
           v="drop view "+view +";"
           print(v+"++++++++++")
           self.initClass.DB.execute_View(v)



    def PrepareRules_Primary_get_sql_queries(self):
        RuleCounter=0;
        while RuleCounter < len(self.Rules):
            # just Header
            if len(self.Rules[RuleCounter].Body) == 0 :
              f=0
            else:
                if not self.Rules[RuleCounter].IsRecusive :
                    self.Rules[RuleCounter]= self.EvaluteRule(self.Rules[RuleCounter])
            RuleCounter+=1




    def Execute(self,Query):
        Fact=self.DatalogParserT.toPredicate(Grammar().literal.parseString(Query))
        RuleT=Rule()
        RuleT.Head=Fact
        return self.get_rule_queries(RuleT)



    def get_rule_queries(self,RuleT):
        for R in self.Rules:
            if R.Head.Name==RuleT.Head.Name:
                if not R.IsRecusive:
                    # R rule contains view query and unifications from queries
                    R= self.Unification_query_params_rule(R,RuleT.Head)
                    rows = R.Print_result(self.initClass.DB)
                    break
                else:
                    v=0
                    print ("No execution ")
                  #  self.Rules_to_be_executed.append(R)
                   # for PredicateT in R.Body:
                    #    if PredicateT.alias=="":
                     #       ttt=0
        return rows

    def Unification_query_params_rule(self ,Rule,QueryAsPred):
        #Get the rule with sql query
        #ResRule = self .EvaluteRule(Rule)
        counter=-1
        visited=""
        Rule.Where_clause=""
        for s in QueryAsPred.Slots :
            counter+=1
            if s.Value!="" :
                if Rule.Head.Slots[counter].VariableName!="":
                    Rule.Where_clause += Rule.Head.Slots[counter].VariableName+"= '" +s.Value+"' and "
                    visited="T"

        if  visited != "" :
            Rule.Where_clause=Rule.Where_clause[:-4]

        return  Rule



    def get_result_rows(self):
        return self.initClass.DB.Select(self.Final_query)

    def Execute_select(self,Q):
        return self.initClass.DB.Select(Q)





    def PrepareRules_generate_alias_for_predicate_by_its_tablename(self):
        RulesCounter=0;
        PredicatCounter=0
        x=0
        # initialize alias name for each predicate
        for Rule in self.Rules:
            x=0
            while x < len(self.Rules[RulesCounter].Body):
                found=None
                if self.Rules[RulesCounter].Body[x].__class__== Predicate:
                    for table in Maps.tables:
                          if table.name.upper() == self.Rules[RulesCounter].Body[x].Name.upper():
                            self.Rules[RulesCounter].Body[x].alias="table_ins%s" %PredicatCounter
                            #print(self.Rules[RulesCounter].Body[x].Name+"  "+ self.Rules[RulesCounter].Body[x].alias)
                            PredicatCounter+=1
                            self.Rules[RulesCounter].sql_tables+=self.Rules[RulesCounter].Body[x].Name +" \""+ self.Rules[RulesCounter].Body[x].alias +"\" ,"
                            found= True
                            break
                    if not found:
                        for view in Maps.views:
                            if view.name.upper() == self.Rules[RulesCounter].Body[x].Name.upper():
                                self.Rules[RulesCounter].Body[x].alias="view_ins%s" %PredicatCounter
                                PredicatCounter+=1
                                self.Rules[RulesCounter].sql_tables+= view.alias +" \""+ self.Rules[RulesCounter].Body[x].alias +"\" ,"
                                break






                x+=1
            self.Rules[RulesCounter].sql_tables=self.Rules[RulesCounter].sql_tables[:-1]
            RulesCounter+=1



    def PrepareRules_create_views_for_primary_rules(self):
        RuleCounter=0;
        while RuleCounter < len(self.Rules):
            # just Header
            if len(self.Rules[RuleCounter].Body) == 0 :
              f=0
            else:
                if not self.Rules[RuleCounter].IsRecusive :
                    ViewName= self.Rules[RuleCounter].View_name
                    view="create or replace view "+ViewName+" as ( select  "

                    for slotz in self.Rules[RuleCounter].Head.Slots :
                        if slotz.VariableName !="" :
                            found=None
                            for alias in  self.Rules[RuleCounter].Head.Non_repeated_perdicate_variables:
                                if alias.Var_name  == slotz.VariableName :
                                    view += alias.table_alias+" as "+ slotz.VariableName+" ,"
                                    found=True
                                    break
                            if not found:
                                view += " \' \' as "+ slotz.VariableName+" ,"
                    view =view [:-1]
                    view += " from " + self.Rules[RuleCounter].get_Query()+" )"
                    #print(view)
                    self.initClass.DB.execute_View(view)
                    self.Rules[RuleCounter].View_query=view

            RuleCounter+=1



    def PrepareRules_generate_View_alias_for_rule_header(self):
        RulesCounter=0;
        Columns=[]
        while RulesCounter < len(self.Rules):
            Columns=[]
            self.Rules[RulesCounter].Body
            View_alias="YADI_DMKM_V_"+self.Rules[RulesCounter].Head.Name + "_"+str(RulesCounter)
            self.Rules[RulesCounter].View_name=View_alias
            self.Views_list.append(View_alias)
            for slotx in self.Rules[RulesCounter].Head.Slots:
                S=Slot(slotx.Value + slotx.VariableName)
                Columns.append(S)
            view1=view(self.Rules[RulesCounter].Head.Name,View_alias,Columns)
            Maps.views.append(view1)
            RulesCounter+=1




    def PrepareRules_check_primary_rules(self):
        #check primary rules 1- no body   2- all predicate in the body are tables
        RuleCounter=0;
        while RuleCounter < len(self.Rules):
            # just Header
            if len(self.Rules[RuleCounter].Body) ==0 :
                Found="F"
                for i in Maps.tables:
                    if i.name.upper()==self.Rules[RuleCounter].Head.Name.upper():
                        self.Rules[RuleCounter].IsPrimary= True
                        Found="T"
                        break;
                if Found=="F":
                    self.Rules[RuleCounter].IsPrimary= None
                    #raise Exception ("There is rule without body and the name of Header not existing in the database schema");
            else:
                BodyCounter=0
                while BodyCounter < len(self.Rules[RuleCounter].Body):
                    if any ( self.Rules[RuleCounter].Head.Name in s.Name for s in self.Rules[RuleCounter].Body):
                        self.Rules[RuleCounter].IsPrimary= None
                        self.Rules[RuleCounter].IsRecusive= True
                        break;

                    if any ( self.Rules[RuleCounter].Body[BodyCounter].Name in s.name for s in Maps.tables) :
                        self.Rules[RuleCounter].IsPrimary= True
                    else:
                        self.Rules[RuleCounter].IsPrimary= None
                        break;
                    BodyCounter+=1

            RuleCounter+=1


    def get_Column_name(self,tableName,index):
        for i in Maps.tables:
            i.__class__=table
            if i.name.upper()==tableName.upper():
                return i.Arrenged_Columns[index]
        for i in Maps.views:
            i.__class__=view
            if i.name.upper()==tableName.upper():
                return i.Arrenged_Columns[index].VariableName




    def PrepareRules_Body_slots_alias_names(self):
        RuleCounter=0;
        while RuleCounter < len(self.Rules):
            List_Counter=0
            while List_Counter < len(self.Rules[RuleCounter].Body):
                self.Rules[RuleCounter].Body[List_Counter].Non_repeated_perdicate_variables=[]
                if self.Rules[RuleCounter].Body[List_Counter].__class__ == Predicate  and  len(self.Rules[RuleCounter].Body[List_Counter].Slots )>= 1 :
                    inner_Counter_1 = 0
                    while inner_Counter_1 < len(self.Rules[RuleCounter].Body[List_Counter].Slots):
                        if self.Rules[RuleCounter].Body[List_Counter].Slots[inner_Counter_1].VariableName != "" and self.Rules[RuleCounter].Body[List_Counter].alias !="":
                                ## get list of predicate's variables avoid replication
                                if not(any( self.Rules[RuleCounter].Body[List_Counter].Slots[inner_Counter_1].VariableName in s.Var_name for s in self.Rules[RuleCounter].Body[List_Counter].Non_repeated_perdicate_variables )) :
                                    perdicate_variable1= perdicate_variable()
                                    perdicate_variable1.Var_name=self.Rules[RuleCounter].Body[List_Counter].Slots[inner_Counter_1].VariableName
                                    perdicate_variable1.table_alias =self.Rules[RuleCounter].Body[List_Counter].alias +"."+self.get_Column_name(self.Rules[RuleCounter].Body[List_Counter].Name,inner_Counter_1)+""
                                    self.Rules[RuleCounter].Body[List_Counter].Non_repeated_perdicate_variables.append(perdicate_variable1)
                        inner_Counter_1+=1
                List_Counter+=1
            RuleCounter+=1


    def PrepareRules_Primary_get_Head_slots_relations_with_body(self):
        #just for primary slots
        RuleCounter=0;
        while RuleCounter < len(self.Rules):
            if not self.Rules[RuleCounter].IsRecusive :
                slots_Counter=0
                self.Rules[RuleCounter].Head.Non_repeated_perdicate_variables=[]
                while slots_Counter < len(self.Rules[RuleCounter].Head.Slots):
                    if self.Rules[RuleCounter].Head.Slots[slots_Counter].VariableName != "" and not(any( self.Rules[RuleCounter].Head.Slots[slots_Counter].VariableName in s.Var_name for s in self.Rules[RuleCounter].Head.Non_repeated_perdicate_variables )) :
                        Found= None
                        for predicateT in self.Rules[RuleCounter].Body :
                            if not Found:
                                for perdicate_variable1 in predicateT.Non_repeated_perdicate_variables:
                                    if  perdicate_variable1.Var_name == self.Rules[RuleCounter].Head.Slots[slots_Counter].VariableName:
                                        Found= True
                                        perdicate_variableT= perdicate_variable()
                                        perdicate_variableT.Var_name=perdicate_variable1.Var_name
                                        perdicate_variableT.table_alias=perdicate_variable1.table_alias
                                        self.Rules[RuleCounter].Head.Non_repeated_perdicate_variables.append(perdicate_variableT)
                    else:
                        if self.Rules[RuleCounter].Head.Slots[slots_Counter].VariableName == "" :
                                        Found= True
                                        perdicate_variableT= perdicate_variable()
                                        perdicate_variableT.Var_name=perdicate_variable1.Var_name
                                        perdicate_variableT.table_alias="\" \""
                                        self.Rules[RuleCounter].Head.Non_repeated_perdicate_variables.append(perdicate_variableT)
                    slots_Counter+=1
            RuleCounter+=1






    def EvaluteRule(self ,Rule):
        List_Counter=0
        # scan the Body to search for shared  variables between the predicates    r1(X,Y):-pred1(X,Z),pred2(Z,Y)
        while List_Counter < len(Rule.Body):
            if Rule.Body[List_Counter].__class__ == Predicate :
                    ## make internal scan between the predicate variables its self
                    if len(Rule.Body[List_Counter].Slots )>= 1:
                        inner_Counter_1 = 0
                        while inner_Counter_1 < len(Rule.Body[List_Counter].Slots):
                            if Rule.Body[List_Counter].Slots[inner_Counter_1].VariableName != "" :
                                inner_Counter_2 = 0
                                while inner_Counter_2 < inner_Counter_1 :
                                    if Rule.Body[List_Counter].Slots[inner_Counter_2].VariableName==Rule.Body[List_Counter].Slots[inner_Counter_1].VariableName :
                                        Rule.sql_condition += Rule.Body[List_Counter].alias +"."+ self.get_Column_name(Rule.Body[List_Counter].Name,inner_Counter_1) +" = "+ Rule.Body[List_Counter].alias +"."+ self.get_Column_name(Rule.Body[List_Counter].Name,inner_Counter_2) +" and "
                                    inner_Counter_2+=1
                            else:
                                if any( Rule.Body[List_Counter].alias in s.name for s in Maps.tables):
                                    Rule.sql_condition += Rule.Body[List_Counter].alias +"."+ self.get_Column_name(Rule.Body[List_Counter].Name,inner_Counter_1) + " = '"+ Rule.Body[List_Counter].Slots[inner_Counter_1].Value +"' and "
                                else:
                                    if any( Rule.Body[List_Counter].Name in s.name for s in Maps.views)  :
                                        Rule.sql_condition += Rule.Body[List_Counter].alias +"."+ self.get_Column_name(Rule.Body[List_Counter].Name,inner_Counter_1) + " = '"+ Rule.Body[List_Counter].Slots[inner_Counter_1].Value +"' and "

                                  # Rule.Body[List_Counter].alias in tables or (in views + has value for variablename in the map with body )

                            inner_Counter_1+=1
            else:
                if Rule.Body[List_Counter].__class__ == Expression :       ##   in case the variable is defined before the condition
                    for RU in Rule.Body:
                        if RU.__class__ == Predicate :
                            if any( Rule.Body[List_Counter].Literals[0] in s.Var_name for s in RU.Non_repeated_perdicate_variables ):
                                for val1 in  RU.Non_repeated_perdicate_variables:
                                    if val1.Var_name==Rule.Body[List_Counter].Literals[0]:
                                        Rule.sql_condition += val1.table_alias+" "+Rule.Body[List_Counter].Literals[1]+ " '"+Rule.Body[List_Counter].Literals[2]+"' and "
                                        break;

            List_Counter+=1
        #print("----------------------------------")

        ## search for relation with previous predicates' slots "variable"
        List_Counter=1
        if len(Rule.Body) > 1 :
            while List_Counter < len(Rule.Body) :
                if Rule.Body[List_Counter].__class__ != Predicate:
                    List_Counter+=1
                    continue

                Variable_Counter=0
                while Variable_Counter < len(Rule.Body[List_Counter].Non_repeated_perdicate_variables):
                            #print("   "+Rule.Body[List_Counter].Non_repeated_perdicate_variables[Variable_Counter].Var_name)
                            List_Counter_2=0
                            while List_Counter_2 < List_Counter:
                                Variable_Counter_2=0
                                while Variable_Counter_2 < len(Rule.Body[List_Counter_2].Non_repeated_perdicate_variables):
                                    ##print(Rule.Body[List_Counter].Non_repeated_perdicate_variables[Variable_Counter].Var_name)
                                    ##print(Rule.Body[List_Counter_2].Non_repeated_perdicate_variables[Variable_Counter_2].Var_name)
                                    if Rule.Body[List_Counter].Non_repeated_perdicate_variables[Variable_Counter].Var_name==Rule.Body[List_Counter_2].Non_repeated_perdicate_variables[Variable_Counter_2].Var_name:
                                        Rule.sql_condition +=Rule.Body[List_Counter].Non_repeated_perdicate_variables[Variable_Counter].table_alias +" = " + Rule.Body[List_Counter_2].Non_repeated_perdicate_variables[Variable_Counter_2].table_alias  +" and "
                                    Variable_Counter_2+=1
                                List_Counter_2+=1
                            Variable_Counter+=1
                List_Counter+=1

        Rule.sql_condition=Rule.sql_condition[:-4]
        return Rule







