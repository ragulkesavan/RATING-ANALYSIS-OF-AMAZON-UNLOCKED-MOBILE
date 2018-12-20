#BAR CHART COMPANY VS TOP RATED AND CO OF REVIEWS

import matplotlib.pyplot as plt
import sqlite3
con=sqlite3.connect('test.db')

a1=con.execute("select name,customers from companies")
b1=a1.fetchall()
c1={key:val for key,val in b1}

#Barchart
plt.bar(range(len(c1)), list(c1.values()), align='center')
plt.xticks(range(len(c1)), list(c1.keys()))
plt.show()
