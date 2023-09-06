# Find the Highest Altitude
'''
There is a biker going on a road trip. The road trip 
consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where 
gain[i] is the net gain in altitude between points i and i + 1 
for all (0 <= i < n). Return the highest altitude of a point.


Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. 
The highest is 1.


Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. 
The highest is 0.
 
'''

# -------sol--------prefix sum probelm------------TC=O(n)------

# we have to start by altitude 0 , which will be our cur_altitude
# initialize a variable highest_altitude = cur_altitude

# increase this cur_altitude with the prefix sum of gain array
# at each iteration update the highes_altitude accordingly
# finally return the highest altitude

def high_alitiude(gains):
    cur_gain = 0
    highest_gain = cur_gain
    
    for gain in gains:
        cur_gain += gain
        highest_gain = max(cur_gain,highest_gain)
        
    return highest_gain

print(high_alitiude([-5,1,5,0,-7]))   #1
print(high_alitiude([-4,-3,-2,-1,4,3,2]))  #0