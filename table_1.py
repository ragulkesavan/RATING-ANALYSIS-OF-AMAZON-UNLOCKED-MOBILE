#TABLE FOR COMPANY BRAND AND OVERALL RATING

#import     textabbale
import sqlite3
from texttable import Texttable

t = Texttable()
con=sqlite3.connect('test.db')
a1=con.execute("Select name,rating from companies")
b1=a1.fetchall()
l=[]

l.append(['BRAND','RATING'])

for i in b1:
    l.append([i[0],i[1]])
t.add_rows(l)
print(t.draw())