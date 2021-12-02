import csv 
import random
import pandas as pd
from pandas.io.parquet import FastParquetImpl
import time
start_time=time.time()

newlist=[]
name=[]
with open('baby-names.csv','r') as f:
    data1=f.readlines()
    count=0
    for i in data1:
       # print(i)
        newlist.append(i.split())
        name.append(newlist[count][0].split(',')[1].strip('"'))
        #stripped_string = a_string.strip('"')
        count=count+1

#2000000  2000000 3000000

# print(name)  10000000 20000000
fname=[]
for i in range(10000000):
    fname.append(random.choice(name))


slist=[]
sname=[]
    #print(newlist)
with open('most-common-name_surnames.csv','r') as f:
    data2=f.readlines()
    count=0
    for i in data2:
        slist.append(i.split())
        sname.append(slist[count][0].split(',')[1].strip('"'))
        count=count+1
    #print(sname)

lname=[]
for i in range(10000000):
    lname.append(random.choice(sname))

phone=[]
digit=['1','2','3','4','5','6','7','8','9','0']
digit1=['6','7','8','9']

for i in range(10000000):
    str=""
    for i in range (10):
        if i==0:
            str+=random.choice(digit1)
        else:

            str+=random.choice(digit) 
    phone.append(str)
#print(phone)
clist=[]
city=[]
with open('Indian_Cities_Database.csv','r',encoding='utf8',errors='ignore') as f:
    data3=f.readlines()
    count=0
    for i in data3:
        clist.append(i.split())
        city.append(clist[count][0].split(',')[0])
        count=count+1
    #print(city)
        
cityname=[]

for i in range(10000000):
    cityname.append(random.choice(city))

gender=[]
g=['MALE','FEMALE']
for i in range(10000000):
    gender.append(random.choice(g))
#print(gender)

age=[]
for i in range(10000000):
    age.append(random.randint(18,90))


sno=[]
for i in range(1,10000001):
    sno.append(i)



df=pd.DataFrame({'S.No.':sno,'FName':fname,'LName':lname,'Gender':gender,'Age':age,'City':cityname,'Phone':phone})
print('Dara')  
print(df)
df.to_csv('1crore.csv',index=False)

# with open('5lakh.csv','w',encoding='utf8',errors='ignore') as file:
#     obj1=csv.writer(file,delimiter='\t')
#     obj1.writerow('Sno  FirstName   LastName    City    Phone   Gender  ')
    
        




end=time.time()
time_taken=end-start_time
print(time_taken)

    


