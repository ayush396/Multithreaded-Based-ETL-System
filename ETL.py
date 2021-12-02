import threading 
import os 
import pandas as pd 
import time 
import multiprocessing
from queue import Queue
q=Queue()
numberOfCores=multiprocessing.cpu_count()
N=2
#print(numberOfCores)

start_time=time.time()

activeThreads=threading.active_count()

def extract(filename):
    inputputFileName = "Split(20)-1crore/"  + filename

    df=pd.read_csv(inputputFileName,delimiter=',')
    q.put(df)



    #500000

def transform(df):
    size=int(10000000/20)
    fname=[]
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

    

def load(df,filename):
    outputFileName = "game3/" + filename
    df.to_csv(outputFileName,index=False)



    #return None


def etl(filename,i):
    
    t1=threading.Thread(target=extract,args=(filename,))
    t1.start()
    t1.join()

    df=q.get()
    #q.pop()
    t2=threading.Thread(target=transform,args=(df,))
    t2.start()
    t2.join()


    t3=threading.Thread(target=load,args=(df,filename,))
    t3.start()
    t3.join()



#print("Program Started....")
allFiles = os.listdir("Split(20)-1crore/")
#print('All Files ',allFiles)
i = 1

for fileName in allFiles:
    #print("File Processing %d (%s)" % (i, fileName))

    t = threading.Thread(target=etl, args=(fileName,i,))
    t.start()

    i = i + 1
    while True:
        #print('Threadng active-> ',threading.active_count())
        if threading.active_count() - activeThreads + 1 <= 6:
            break
        time.sleep(0.0001)


# Waiting to finish all Threads
while True:
    if threading.activeCount() == activeThreads:
        break
    else:
        #print("...Thread Left %d..." % (threading.activeCount() - activeThreads))
        time.sleep(0.0001)

#print("All Threads compeleted")
print("\nTotal Time %f sec" % (round(time.time() - start_time, 4)))
print("Program Finished")
