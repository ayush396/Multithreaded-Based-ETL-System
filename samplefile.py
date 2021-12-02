import os
import time, threading, multiprocessing
startTime = time.time()

activeThreads = threading.activeCount()
print(activeThreads)
numberOfCores = multiprocessing.cpu_count()
N = 2
print("Number Of Threds per Cores = ", N, "\n")

def transform(fileName):
    inputputFileName = "Split(20)-10lakh/"  + fileName
    outputFileName = "dir(20)-10lakh/" + fileName
    fpr = open(inputputFileName,'r')
    fpw = open(outputFileName, 'w')
    count=1
    for line in fpr:
        str=""
        str+='(+91)-'+line.split()[0].split(',')[6]
        #print(str)
        #line.split()[0].split(',')[6]=str
        #line.replace(line.split()[0].split(',')[6],str).upper()).split()[0].split(',')[3]
        str1=''
        if count>1:
            if line.split()[0].split(',')[3]=='MALE':
                str1='M'
            elif line.split()[0].split(',')[3]=='FEMALE':
                str1='F'
            fpw.write(line.upper().replace(line.split()[0].split(',')[6],str).replace(line.upper().replace(line.split()[0].split(',')[6],str).split()[0].split(',')[3],str1))
        else:
            fpw.write(line.upper())

        count+=1

    fpr.close()
    fpw.close()
    return None



# Main Program
print("Program Started....")
allFiles = os.listdir("Split(20)-10lakh/")
print('All Files ',allFiles)
i = 1
for fileName in allFiles:
    print("File Processing %d (%s)" % (i, fileName))
    print('Threadng active-> ',threading.active_count())
    #if threading.activeCount() - activeThreads + 1 <= N * numberOfCores:

    t = threading.Thread(target=transform, args=(fileName,))
    t.start()
        #t.join()

    
    i = i + 1
    while True:
        print('Threadng active-> ',threading.active_count())
        if threading.activeCount() - activeThreads + 1 <= N * numberOfCores:
            break
        time.sleep(1)

# # Waiting to finish all Threads
while True:
    if threading.activeCount() == activeThreads:
        break
    else:
        print("...Thread Left %d..." % (threading.activeCount() - activeThreads))
        time.sleep(0.0000000001)

print("All Threads compeleted")
print("\nTotal Time %f sec" % (round(time.time() - startTime, 4)))
print("Program Finished")