import pandas  as pd
import csv
import time 
import os
start=time.time()
def trasnform(file):
    inputputFileName = "Split(10)-1crore/"  + file
    df=pd.read_csv(inputputFileName,delimiter=',')
    cname=df.columns
    #for i in range(df.shape[0]):
    fname=[]
    size=int(10000000/10)
    for i in range(size):
        fname.append(df['FName'][i].lower())
    df['FName']=fname

    lname=[]
    for i in range(size):
        lname.append(df['LName'][i].lower())
    df['LName']=lname

    sex=[]
    for i in range(size):
        if df['Gender'][i]=='MALE':
            sex.append('M')
        else:
            sex.append('F')
   

    df['Gender']=sex
    
    
    city=[]
    for i in range(size):
        city.append(df['City'][i].upper())
    df['City']=city
   
    
    phone=[]
    for i in range(size):
        phone.append('(+91)-'+str(df['Phone'][i]))
    df['Phone']=phone

    outputFileName = "game3/" + file
    df.to_csv(outputFileName,index=False)

        
#     print(df)

    
# def transform(file,i):
#     inputputFileName ='Split(10)-5Lakh/'+file
#     outputFileName = 'trans-50lakh/'+'output_{}.csv'.format(i)
#     fpr = open(inputputFileName,'r')
#     fpw = open(outputFileName, 'w')
#     count=1
#     for line in fpr:
#         str=""
#         str+='(+91)-'+line.split()[0].split(',')[6]
#         #print(str)
#         #line.split()[0].split(',')[6]=str
#         #line.replace(line.split()[0].split(',')[6],str).upper()).split()[0].split(',')[3]
#         str1=''
#         if count>1:
#             if line.split()[0].split(',')[3]=='MALE':
#                 str1='M'
#             elif line.split()[0].split(',')[3]=='FEMALE':
#                 str1='F'
#             fpw.write(line.upper().replace(line.split()[0].split(',')[6],str).replace(line.upper().replace(line.split()[0].split(',')[6],str).split()[0].split(',')[3],str1))
#         else:
#             fpw.write(line.upper())

#         count+=1

#     fpr.close()
#     fpw.close()
#     return None


if __name__=='__main__':
    allFiles = os.listdir("Split(10)-1crore/")
    i=1
    for file in allFiles:
        trasnform(file)
        i+=1
    final=time.time()
    total=final-start
    print(total)



















  