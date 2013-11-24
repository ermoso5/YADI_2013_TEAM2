from sqlalchemy import *

db = create_engine('postgresql://postgres:dmkm@localhost:5432/Datalog') # I create a database named Datalog and the code is dmkm in postgreSQL

db.echo = False  # if we want to see the SQL we're creating, the value should be True

metadata = MetaData(db)


p = Table('p', metadata,
        Column('id', Integer, primary_key=True),
        Column('col1', String(15)),
        Column('col2', String(15)),
)
p.create()

i = p.insert()
i.execute({'id': 1, 'col1': 'a','col2':'b'},
              {'id': 2, 'col1': 'b','col2':'c'},
              {'id': 3, 'col1': 'e','col2':'e'},
              {'id': 4, 'col1': 'g','col2':'j'})

s1 = p.select()
rs1 = s1.execute()

row = rs1.fetchone()
print('p_table')
print('-----------------------------')

print (row.id,'|', row.col1,'|', row.col2)
for row in rs1:
    print (row.id,'|', row.col1,'|', row.col2)
print('')

r = Table('r', metadata,
        Column('id', Integer, primary_key=True),
        Column('col3', String(15)),
        Column('col4', String(15)),
)
r.create()

i = r.insert()
i.execute({'id': 1, 'col3': 'b','col4':'c'},
              {'id': 2, 'col3': 'g','col4':'j'},
              {'id': 3, 'col3': 'e','col4':'f'})

s2 = r.select()
rs2 = s2.execute()

row = rs2.fetchone()
print('r_table')
print('-----------------------------')

print (row.id,'|', row.col3,'|', row.col4)
for row in rs2:
    print (row.id,'|', row.col3,'|', row.col4)
print('')
        
s = Table('s', metadata,
        Column('id', Integer, primary_key=True),
        Column('col5', String(15)),
        Column('col6', String(15)),
)
s.create()

i = s.insert()
i.execute({'id': 1, 'col5': 'a','col6':'b'},
              {'id': 2, 'col5': 'j','col6':'g'},
              {'id': 3, 'col5': 'f','col6':'e'},
              {'id': 4, 'col5': 'c','col6':'b'})
####################
s3 = s.select()
rs3 = s3.execute()

row = rs3.fetchone()
print('s_table')
print('-----------------------------')

print (row.id,'|', row.col5,'|', row.col6)
for row in rs3:
    print (row.id,'|', row.col5,'|', row.col6)
print('')
