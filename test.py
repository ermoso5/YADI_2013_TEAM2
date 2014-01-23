from MainPKG.Parser import *
#DatalogParser("C:\Python33\Rules.txt").GetRuleFromQuery("q(X,Y).")
DatalogParser("C:\Python33\Rules.txt").toRule("q(x,Y).").print()
print()
DatalogParser("C:\Python33\Rules.txt").toRule("q(X,Y):- follower(X,Y).").print()
print()
print(DatalogParser("C:\Python33\Rules.txt").toFact("q1(1,2).").Slots)
print()
t = DatalogParser("C:\Python33\Rules.txt").toFact("q1(x,y).").Slots[1]
t1 = DatalogParser("C:\Python33\Rules.txt").checkSafety("q(X,Y):- follower(X,Z).")#.toFact("q1(x,y).").Slots[1]
print(t1)
print("m")
DatalogParser("C:\Python33\Rules.txt").toRule("q(X, Y):- follower(X,Z).").print()

#DatalogParser("C:\Python33\Rules.txt").GetRuleFromQuery("q(X,Y).").print() #toFact("q1(x,y).").Slots[2].print()
print()
#print(Grammar().fact.parseString("xt(X,Y)."))
#print(Grammar().expression.parseString("x<y"))
#print(Grammar().expression.parseString("x>=y"))
#print(Grammar().expression.parseString("x<y"))
#print(Grammar().expression.parseString("x!=y"))
#print(Grammar().expression.parseString("x=y"))
#print(Grammar().expression.parseString("x+y is z"))
#print(Grammar().expression.parseString("x+y>z+f"))

#print(Grammar().rule.parseString('student_book(N1,Z):-student(X,N1),sTD_book(W,X,Y),book(Y,Z).'))
#print(Grammar().rule.parseString('student_book(N1,Z).'))
#student_book(N1,Z):-student(X,N1),STD_book(W,X,Y),book(Y,Z).
print(Grammar().no_body_rule.parseString('student_book(1,2).'))

#Grammar().literal.parseString(['follower', 'X', 'Y'])

#from tkinter import *

#root = Tk()

#scrollbar = Scrollbar(root)
#scrollbar.pack(side=RIGHT, fill=Y)

#listbox = Listbox(root)
#listbox.pack()

#for i in range(100):
 #   listbox.insert(END, i)

# attach listbox to scrollbar
#listbox.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=listbox.yview)

#mainloop()