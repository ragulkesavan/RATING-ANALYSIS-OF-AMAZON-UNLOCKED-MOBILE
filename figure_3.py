#PIE CHART COMPANY VS RATING AND NO OF CUST

import sqlite3
import matplotlib.pyplot as plt
con=sqlite3.connect('test.db')
a1=con.execute("Select name,customers from companies")
b1=a1.fetchall()
print(b1)

c1={key:val for key,val in b1}
con.close()
labels = list(c1.keys())
sizes = list(c1.values())
colors = ['gold', 'yellowgreen', 'orange', 'blue', 'red']
exploe = (0.05,0.05,0.05)

#PIE CHAART
plt.pie(sizes, explode=None,labels=labels,colors=colors, shadow=True, startangle=140)
plt.axis('equal')
plt.show()