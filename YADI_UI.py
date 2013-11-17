from tkinter import *
#from tkinter.ttk import *
from Parser import *

def load_rules():    
    filename = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')], initialdir = "C:/Python33")
    if filename: 
        try:
            rule_file = open(filename).read()
            Label(rules, text=rule_file, bg="white", width=200).pack()
            filename.close()
            parser = DatalogParser(filename)
        except: 
            tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename) 

def execute():
    parser.setQuery(query_inp.get())
    #Convert to SQL and evaluate

#create the window
master = Tk()

#styles for window
master.title("YADI")
master.geometry("400x400")

#set definition mode

definition_mode = Frame(master, width=400)
definition_mode.pack()

Label(definition_mode, text="Rules").pack()

rules = Frame(definition_mode, width=400, height=200, bg="white")
rules.pack()

rule_loader = Button(definition_mode, text="Select your file", command=load_rules)
rule_loader.pack(side=RIGHT)

#set query mode
query_mode = Frame(master, width=400, height=80)
query_mode.pack()

query_lb = Label(query_mode, text="Query").pack()
query_inp = Entry(query_mode, width=200, bg="white")
query_inp.pack()

executer = Button(query_mode, text="Execute", command=execute)
executer.pack(side=RIGHT)

#results
results = Frame(master, width=400)
results.pack()

Label(results, text="Results").pack()

result_block = Frame(results, width=300, height=60, bg="white")
result_block.pack()

master.mainloop()

