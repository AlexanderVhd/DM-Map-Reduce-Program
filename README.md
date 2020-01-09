# DM-Map-Reduce-Program
Overview: This program reads from a CSV file that contains tweets, in this case the local csv file contains Trump tweets (over 7000 tweets), and calculates the frequency of words that are used in all the tweets using the map reduce algorithm. There are two ways the map reduce algorithm counts the words: sequentially and in parrallel (parallel method involves multiple cores performing the counting tasks). The user can choose which method to count the words. 

Language used: Python for both sequential and distributed 

Distributed Solution: I used multiprocessing instead of Hadoop for the solution which involved importing the module and using the pool 
class to map the sublists. I used pool.imap_unordered instead of pool.map since the it makes the processes independant and doesn't wait for the other processes' results to execute which makes it slightly faster than pool.map 

User selects their counting method
![image](https://user-images.githubusercontent.com/34779092/72037566-bb647080-326c-11ea-804a-135ede8cafcf.png)

User selects sequential method
![image](https://user-images.githubusercontent.com/34779092/72037398-03cf5e80-326c-11ea-8969-cf4eb5e7e29d.png)

User selects parallel method
![image](https://user-images.githubusercontent.com/34779092/72037434-2a8d9500-326c-11ea-8b20-731ff3f79697.png)
