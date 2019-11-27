# DM-Map-Reduce-Program
Members: Alexander Vahid (991445119)
Language: Python for both sequential and distributed 
Distributed Solution: I used multiprocessing instead of Hadoop for the solution which involved importing the module and using the pool 
class to map the sublists. I used pool.imap_unordered instead of pool.map since the it makes the processes independant and doesn't wait for
the other processes' results to execute which makes it slightly faster than pool.map 
