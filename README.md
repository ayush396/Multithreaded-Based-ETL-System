# Multithreaded-Based-ETL-System
**What is Multi-Threading?**
Multithreading is a model of program execution that allows for multiple threads to be 
created within a process, executing independently but concurrently sharing process resources. 
Depending on the hardware, threads can run fully parallel if they are distributed to their own CPU core.

**What is ETL?**
![image](https://user-images.githubusercontent.com/83595522/144435081-20ae3ffc-1240-430b-b776-6bda49fd99d4.png)



Exclusively, we implemented ETL aka Extract-Transform-Load using multi-threading where a large number of files are processed.
Besides entire processing of the file at once, ETL allows us to run extract, transform and load simultaneously using three threads independently.
Above Diagram illustrates the sequence of threads executing at a single instance 
At instance3,1st file is loading 2nd  file is transforming 3rd file is extracting

