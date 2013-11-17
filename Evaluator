from MainPKG.Basic_Classes import *
              
class Evalute:
    sql_condition=""
    sql_tables="select * from "
    def get_Column_name(self,tableName,index):
        for i in Maps.tables:
            i.__class__=table
            if i.name.upper()==tableName.upper():
                return i.Arrenged_Columns[index]
           
    def evalute(self ,Rule):
        List_Counter=0
        x=0
       
        ## initialize alias name for each predicate 
        while x < len(Rule.Body):
            if Rule.Body[x].__class__== Predicate:
                Rule.Body[x].alias="table%s" %x
                self.sql_tables+=Rule.Body[x].Name +" "+ Rule.Body[x].alias +" ,"
            x+=1
        self.sql_tables=self.sql_tables[:-1]                  
        ## scan the Body to search for shared  variables between the predicates
        while List_Counter < len(Rule.Body):
            if Rule.Body[List_Counter].__class__ == Predicate :
                    ## make internal scan between the predicate variables its self 
                    Rule.Body[List_Counter].Non_repeated_perdicate_variables=[]
                    #print("      "+Rule.Body[List_Counter].Name)
                    if len(Rule.Body[List_Counter].Slots )>= 1:
                        inner_Counter_1 = 0
                        while inner_Counter_1 < len(Rule.Body[List_Counter].Slots):
                            if Rule.Body[List_Counter].Slots[inner_Counter_1].VariableName != "" : 
                                ## get list of predicate's variables avoid replication
                                #print(Rule.Body[List_Counter].Slots[inner_Counter_1].VariableName )
                                #print("*********************")
                                #for s in Rule.Body[List_Counter].Non_repeated_perdicate_variables:
                                    #print( s.Var_name)
                                #print("*********************")
                                if not(any( Rule.Body[List_Counter].Slots[inner_Counter_1].VariableName in s.Var_name for s in Rule.Body[List_Counter].Non_repeated_perdicate_variables )) :
                                    #print("In")     ##print("inner "+ inner_Counter_1.__str__())
                                    perdicate_variable1= perdicate_variable()
                                    perdicate_variable1.Var_name=Rule.Body[List_Counter].Slots[inner_Counter_1].VariableName
                                    perdicate_variable1.table_alias =Rule.Body[List_Counter].alias +".\""+self.get_Column_name(Rule.Body[List_Counter].Name,inner_Counter_1)+"\""
                                    Rule.Body[List_Counter].Non_repeated_perdicate_variables.append(perdicate_variable1)
                                    ##print( Rule.Body[List_Counter].Non_repeated_perdicate_variables[len( Rule.Body[List_Counter].Non_repeated_perdicate_variables)-1].Var_name )
                                    ##print( Rule.Body[List_Counter].Non_repeated_perdicate_variables[len( Rule.Body[List_Counter].Non_repeated_perdicate_variables)-1].table_alias )                                   
                                    ##check for inner relation inside the predicate   F(X,Y,X)
                              
                                inner_Counter_2 = 0
                                while inner_Counter_2 < inner_Counter_1 :
                                    if Rule.Body[List_Counter].Slots[inner_Counter_2].VariableName==Rule.Body[List_Counter].Slots[inner_Counter_1].VariableName :
                                        self.sql_condition += Rule.Body[List_Counter].alias +".\""+ self.get_Column_name(Rule.Body[List_Counter].Name,inner_Counter_1) +"\" = "+ Rule.Body[List_Counter].alias +"."+ self.get_Column_name(Rule.Body[List_Counter].Name,inner_Counter_2) +"\" and "
                                    inner_Counter_2+=1 
                            else:
                                self.sql_condition += Rule.Body[List_Counter].alias +"."+ self.get_Column_name(Rule.Body[List_Counter].Name,inner_Counter_1) + " = '"+ Rule.Body[List_Counter].Slots[inner_Counter_1].Value +"' and "              
   
                            ##print(inner_Counter_1)
                            inner_Counter_1+=1
            else:
                if Rule.Body[List_Counter].__class__ == Expression :       ##   in case the variable is defined before the condition
                    for RU in Rule.Body:
                        if RU.__class__ == Predicate :                                                                             
                            if any( Rule.Body[List_Counter].Literals[0] in s.Var_name for s in RU.Non_repeated_perdicate_variables ):
                                 for val1 in  RU.Non_repeated_perdicate_variables:
                                     if val1.Var_name==Rule.Body[List_Counter].Literals[0]:
                                        self.sql_condition += val1.table_alias+" "+Rule.Body[List_Counter].Literals[1]+ " '"+Rule.Body[List_Counter].Literals[2]+"' and "
                                        break;
                         
            List_Counter+=1
        #print("----------------------------------")
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
                                        self.sql_condition +=Rule.Body[List_Counter].Non_repeated_perdicate_variables[Variable_Counter].table_alias +" = " + Rule.Body[List_Counter_2].Non_repeated_perdicate_variables[Variable_Counter_2].table_alias  +" and "
                                    Variable_Counter_2+=1
                                List_Counter_2+=1
                            Variable_Counter+=1
                List_Counter+=1       
            
        self.sql_condition=self.sql_condition[:-4]
  
  
  
  
  
  
