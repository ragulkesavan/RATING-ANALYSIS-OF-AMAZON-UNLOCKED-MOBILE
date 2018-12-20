#PIE CHART FOR COMPANY VS RATING AND NO OF CUSTOMERS
import sqlite3
import matplotlib.pyplot as plt
con=sqlite3.connect('test.db')

#fetching all data
a=con.execute("Select name,customers from topten_a")
b=a.fetchall()
c1={key:val for key,val in b}
label = list(c1.keys())
size = list(c1.values())
color = ['gold', 'yellowgreen', 'violet', 'orange', 'blue', 'red']
explodes = (0.05,0.05,0.05)

#ploting graph
plt.pie(size, explode=None,labels=label,colors=color, shadow=True, startangle=140)
plt.axis('equal')
plt.show()

