
#import pandas time and sqlite3
import pandas as p
import time
import sqlite3

#connecting database
con=sqlite3.connect('test.db')

#creatring tables
con.execute("Create table topten_a(name text not null,rating real not null,price real not null,customers real not null);")
con.execute("Create table companies(name text not null,rating real,customers integer);")

# starting stopwatch
start_time = time.clock()

#reading the dataset
dataset = p.read_csv('Amazon_Unlocked_Mobile.csv',dtype={"ProductName": str, "Brand": str, 'Price': float, 'Rating': float, 'Review':str, 'ReviewVotes':str});

product=list((dataset.ProductName.unique())) #getting unique list of products

companies=list(dataset.Brand.unique())       #getting unique list of companies

companies_dict={}                            #empty dictionary {company_name:[sum_of_rating,total_no_of_products,company_overall_rating]}
for i in companies:
    companies_dict[i]=[0.0,0,0.0]            #initialising dictionary

finaldict={}                                 #empty dictionay {product:[sum_of_rating,no_of_reviewers,price,mean_rate,brand]}

for i in product:                            #initialising product list
    finaldict[i]=[0.0,0.0,0.0,0.0,'']

for a in dataset.iterrows():               #for each row in dataset
    finaldict[a[1].ProductName][0]=finaldict[a[1].ProductName][0]+float(a[1].Rating)  #storing sum of rate in final_dict
    finaldict[a[1].ProductName][1] = finaldict[a[1].ProductName][1] + 1.0             #storing no of customers
    finaldict[a[1].ProductName][2] = float(a[1].Price)                                #storing price
    finaldict[a[1].ProductName][4] = str(a[1].Brand)                                  #storing brand

for i in product:
    finaldict[i][3]=finaldict[i][0]/finaldict[i][1]                                   #storing the  mean_rate for each product

listk=sorted(finaldict.items(), key=lambda x: x[1][3],reverse=True)                   #sorting by mean_rate


#we need to pick up the top 10 product based on top 10 mean_rating and highest number of reviews
maxrate=5.0
maxtuple=listk[0]
count=0

for i in listk:
    if i[1][4]!='nan':
        companies_dict[i[1][4]][0]=companies_dict[i[1][4]][0]+i[1][3]
        companies_dict[i[1][4]][1] = companies_dict[i[1][4]][1] + 1
    if i[1][3]<maxrate:
        maxrate=i[1][3]
        print(maxtuple)
        #inserting to db
        con.execute("Insert into topten_a(name,rating,price,customers) values(?,?,?,?)",(maxtuple[0],maxtuple[1][3], maxtuple[1][2], maxtuple[1][1]))
        maxtuple=i
        count=count+1
        if count > 10:
            break
    else :
        if maxtuple[1][1] < i[1][1]:
            maxtuple=i

#calculatig the mean_rate for each brand
for i in list(companies_dict.keys()):
    if companies_dict[i][1]!=0:
        companies_dict[i][2]=companies_dict[i][0]/float(companies_dict[i][1])

#sorting based using no of customer reviews
listb=sorted(companies_dict.items(), key=lambda x: x[1][1],reverse=True)

#inserting top 10 companies into db
c=0
for i in listb:
   if c<10:
       con.execute("Insert into companies(name,rating,customers) values(?,?,?)",(i[0], i[1][2], i[1][1]))
       c=c+1
   else :
       break

#stoping stop watch
print(time.clock()-start_time," seconds")
#commit to db
con.commit()
print(listb)
#closing con
con.close()