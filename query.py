@@
@@#Here i build quary.py to test some example
######################### Example 2 ########################
@@# P(X,Y) :- s(X,Y), r(Y,X).
@@# ?- P(X,Y)
from sqlalchemy import *

db = create_engine('postgresql://postgres:dmkm@localhost:5432/Datalog') # I create a database named Datalog and the code is dmkm in postgreSQL

db.echo = False # if we want to see the SQL we're creating, the value should be True

metadata = MetaData(db)

p = Table('p', metadata, autoload=True)
s = Table('s', metadata, autoload=True)
r = Table('r', metadata, autoload=True)

def run(stmt):
rs = stmt.execute()
for row in rs:
print (row)

result = select([r],r.c.col3 == s.c.col6)
print('r_table')
run(result)
print('')

result = select([s],r.c.col3 == s.c.col6)
print('r_table')
run(result)
print('')
