# Number of Recent Calls

'''
You have a RecentCounter class which counts the number 
of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents 
some time in milliseconds, and returns the number of requests that 
has happened in the past 3000 milliseconds (including the new request). 

Specifically, return the number of requests that have happened in the 
inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger 
value of t than the previous call.

 

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3


'''
# we are given a class and RecentCounter
# Inside class we have a constructor and a function ping(int t)

# we will be given an array of pings timings in milisecond

# we have to return the count of pings during the time interval of 
# (t-3000 miliseconds to t miliseconds)


# --------------------solution--------
# firstly we will initialize an empty queue for easy poping from front
# and appending from back in array of item

# In python we can implement queue using deque
from collections import deque

# Step1 :
# Inside the ping function we will first append the t in the queue

# Step2 :
# we will popleft items that are outdated from time interval t-3000

#step3 : 
# finally return len of queue


class RecentCounter: 
    
    def __init__(self):
        self.arr = deque()
        
    
    def ping(self,t)-> int:
        #step1.
        self.arr.append(t)
        
        #step2.
        while self.arr[0]<t-3000:
            self.arr.popleft()
        
        #step3.
        return len(self.arr)


obj =  RecentCounter()

a= obj.ping(1)
b=obj.ping(100)
c=obj.ping(3001)
d=obj.ping(3002)

print(a,b,c,d)
# 1 2 3 3