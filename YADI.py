from tkinter import *
from tkinter import filedialog
from MainPKG.Parser import *
from MainPKG.Evaluator import *
from MainPKG.DatabaseConnection import *

class YADI_UI:
    parser = null
    def load_rules(self):
        self.rules_file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')], initialdir = "C:/Python33")
        if self.rules_file_path:
            try:
                rule_file = open(self.rules_file_path).read()
                Label(self.rules, text=rule_file, bg="white", width=200).pack()
                self.parser = DatalogParser(self.rules_file_path)
            except:
                print("Failed to read file \n'%s'"%self.rules_file_path)

    def execute(self):
        DB=Database()
        DB.DB_name="Tiny_copy" #self.db_name.get()
        DB.DB_user= "postgres" #self.db_user_name.get()
        DB.DB_password="_password" #self.db_password.get()
        DB.loadMap()

        Rs=self.parser.GetRules()
        EC=Evalute()
        query= self.query.get() #"aV(X,Y)"
        F=self.parser.toPredicate(Grammar().literal.parseString(query))

        for R in Rs:
            if R.Head.Name==F.Name:
                EC.evalute(R)
                Label(self.results, text="Query is " + EC.sql_tables+" where "+EC.sql_condition, bg="white", width=200).pack()
                break

        if(len(EC.sql_condition) > 0):
            Rows = DB.Select(EC.sql_tables + " where "+EC.sql_condition)
        else:
            Rows = DB.Select(EC.sql_tables)

        for R in Rows:
            Label(self.results, text=R, bg="white", width=200).pack()

    def __init__(self):
        #create the window
        master = Tk()

        #styles for window
        master.title("YADI")
        master.geometry("400x400")

        #db connection data block
        db_setup = Frame(master, width=400).pack()
        Label(db_setup, text="Enter database name:").pack()
        self.db_name = Entry(db_setup, bg="white")
        self.db_name.pack()
        Label(db_setup, text="Enter user name:").pack()
        self.db_user_name = Entry(db_setup, bg="white")
        self.db_user_name.pack()
        Label(db_setup, text="Enter password:").pack()
        self.db_password = Entry(db_setup, bg="white")
        self.db_password.pack()

        #set definition mode
        definition_mode = Frame(master, width=400).pack()

        Label(definition_mode, text="Rules").pack()

        rules = Frame(definition_mode, width=400,height=100, bg="white")
        rules.pack()

        rule_loader = Button(definition_mode, text="Select your file", command=self.load_rules)
        rule_loader.pack()

        #set query mode
        query_mode = Frame(master, width=400).pack()

        Label(query_mode, text="Query").pack()
        query_inp = Entry(query_mode, width=200, bg="white")
        query_inp.pack()

        executer = Button(query_mode, text="Execute", command=self.execute)
        executer.pack()

        #results
        results = Frame(master, width=400).pack()

        Label(results, text="Results").pack()

        result_block = Frame(results, width=300, bg="white").pack()

        self.definition_mode = definition_mode
        self.query = query_inp
        self.rules = rules
        self.results = result_block
        master.mainloop()

YADI_UI()

