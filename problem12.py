# Container With Most Water
'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented 
by array [1,8,6,2,5,4,8,3,7]. In this case, the max area 
of water (blue section) the container can contain is 49.


Example 2:

Input: height = [1,1]
Output: 1
'''

# ---------------sol1 Brute Force----------TC=O(n^2)-----SC=O(1)--------TLE--
# The basic idea would be to check every possible pair of lines 
# and find the maximum area out of those lines 
# area between each pair of lines i,j = (j-i)*min(height[i],height[j])

# we will check all pairs using two nested loops
# loop i , from 0 to n-2
# loop j , from i+1 to n-1

def MostWater(heights):
    maxArea = 0
    for i in range(0,len(heights)-1):
        for j in range(i+1,len(heights)):
            currArea = (j-i)*min(heights[i],heights[j])
            maxArea = max(currArea,maxArea)
            
    return maxArea

print(MostWater([1,8,6,2,5,4,8,3,7]))  #49
print(MostWater([1,1]))  #1
        
#time complexity is O(n^2) coz for loop inside for loop
#space complexity is O(1), coz we are using a constant number of variables

# ------sol2 -----using two pointers---------TC=O(n)------SC=O(1)------

# initialize maxarea=0,two pointers i,j at start and end of the array
# while i<j
# calculate area = (j-i)*min(height[i],height[j])
# update maxarea , for max of maxarea or cur-area
# if height[i]<height[j] => move i one step forward
# else move j one step backward

def MaxWater(heights):
    maxarea = 0
    i=0
    j=len(heights)-1
    while(i<j):
        curarea = (j-i)*min(heights[i],heights[j])
        maxarea = max(maxarea,curarea)
        if(heights[i]<heights[j]):
            i+=1
        else:
            j-=1
    return maxarea

print(MaxWater([1,8,6,2,5,4,8,3,7]))  #49
print(MaxWater([1,1]))  #1