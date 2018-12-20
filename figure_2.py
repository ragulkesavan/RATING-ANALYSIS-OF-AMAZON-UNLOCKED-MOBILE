#BAR CHART COMPANY VS RATING OF EACH
import matplotlib.pyplot as plt
import sqlite3
con=sqlite3.connect('test.db')


#Fetching data from the table
a1=con.execute("select name,customers from topten_a")
b1=a1.fetchall()
c1={key:val for key,val in b1}

#Barchart
plt.bar(range(len(c1)), list(c1.values()), align='center')
plt.xticks(range(len(c1)), list(c1.keys()))
plt.show()
