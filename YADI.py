from tkinter import *
from tkinter import filedialog
from MainPKG.Parser import *
from MainPKG.Evaluator import *
from MainPKG.DatabaseConnection import *

class YADI_UI:
    parser = None
    def load_rules(self):
        self.rules_file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')], initialdir = "C:/Python33")
        if self.rules_file_path:
            try:
                for child in self.rules.winfo_children():
                    child.destroy()
                rule_file = open(self.rules_file_path).read()
                Label(self.rules, text=rule_file, bg="white").pack()
                self.parser = DatalogParser(self.rules_file_path)
            except:
                print("Failed to read file \n'%s'"%self.rules_file_path)

    def execute(self):
        DB=Database()
        #self.parser = DatalogParser("C:/Python33/Rules.txt")
        DB.DB_name = self.db_name.get() #"Tiny_twitter"
        DB.DB_user = self.db_user_name.get() # "postgres"
        DB.DB_password = self.db_password.get() #"_password"
        DB.loadMap()

        for child in self.results.winfo_children():
            child.destroy()

        try:
            Rs = self.parser.GetRules()
            EC = Evalute()
            query = self.query.get() #"aV(X,Y)"
            F=self.parser.GetRuleFromQuery(query)

            for R in Rs:
                if R.Head.Name==F.Name:
                    EC.evalute(R)
                    Label(self.results, text="Query is " + EC.sql_tables+" where "+EC.sql_condition, bg="white").pack()
                    break

            if(len(EC.sql_condition) > 0):
                Rows = DB.Select(EC.sql_tables + " where "+EC.sql_condition)
            else:
                Rows = DB.Select(EC.sql_tables)


            warnings = open(self.parser.log_file).read()
            Label(self.results, text=warnings, bg="white", fg="red").pack()

            for R in Rows:
                Label(self.results, text=R, bg="white").pack()

        except Exception:
            errors = open(self.parser.log_file).read()
            Label(self.results, text=errors, bg="white", fg="red").pack()


    def __init__(self):
        #create the window
        master = Tk()

        #styles for window
        master.title("YADI")
        master.geometry("400x400")

        #scrollbar
        vscrollbar = AutoScrollbar(master)
        vscrollbar.grid(row=0, column=1, sticky=N+S)
        hscrollbar = AutoScrollbar(master, orient=HORIZONTAL)
        hscrollbar.grid(row=1, column=0, sticky=E+W)

        canvas = Canvas(master, bd=0,yscrollcommand=vscrollbar.set,xscrollcommand=hscrollbar.set)
        canvas.grid(row=0, column=0, sticky=N+S+E+W)

        vscrollbar.config(command=canvas.yview)
        hscrollbar.config(command=canvas.xview)

        # make the canvas expandable
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        main_frame = Frame(canvas)
        main_frame.pack()
        #db connection data block
        db_setup = Frame(main_frame, width=400)
        db_setup.pack()
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
        definition_mode = Frame(main_frame, width=400)
        definition_mode.pack()

        Label(definition_mode, text="Rules").pack()

        rules = Frame(definition_mode, width=400,height=100, bg="white")
        rules.pack()

        rule_loader = Button(definition_mode, text="Select your file", command=self.load_rules)
        rule_loader.pack()

        #set query mode
        query_mode = Frame(main_frame, width=400)
        query_mode.pack()

        Label(query_mode, text="Query").pack()
        query_inp = Entry(query_mode, bg="white")
        query_inp.pack()

        executer = Button(query_mode, text="Execute", command=self.execute)
        executer.pack()

        #results
        results = Frame(main_frame, width=400)
        results.pack()

        Label(results, text="Results").pack()

        result_block = Frame(results, width=300, height=300, bg="white")
        result_block.pack()

        canvas.create_window(0, 0, anchor=NW, window=main_frame)
        result_block.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        self.definition_mode = definition_mode
        self.query = query_inp
        self.rules = rules
        self.results = result_block
        master.mainloop()

class AutoScrollbar(Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        print("Cannot use pack with this widget")
    def place(self, **kw):
        print("Cannot use place with this widget")


YADI_UI()

