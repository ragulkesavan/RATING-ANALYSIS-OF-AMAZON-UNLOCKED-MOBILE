#TABLE FOR TOPTEN PRODEUCTS AND RATING

#IMPORT TABLE
import sqlite3
from texttable import Texttable

t = Texttable()
con=sqlite3.connect('test.db')
a1=con.execute("Select name,rating from topten_a")
b1=a1.fetchall()
l=[]
l.append(['PRODUCT','RATING'])

for i in b1:
    l.append([i[0],i[1]])
t.add_rows(l)

#PRINTING TABLE
print(t.draw())