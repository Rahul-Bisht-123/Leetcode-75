# Unique Number of Occurrences

'''
Given an array of integers arr, return true if 
the number of occurrences of each value in the 
array is unique or false otherwise.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 
2 has 2 and 3 has 1. No two values have the 
same number of occurrences.


Example 2:

Input: arr = [1,2]
Output: false


Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

'''

# ----sol-----
# return true if frequency of each item in array is different
# else return false
def unique_frequency(nums):
    freq={}

#creating a frequency map for the items    
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    keys = list(freq.values())
    duplicates = [i for i in keys if keys.count(i)>1]
    
    return duplicates==[]
    
print(unique_frequency([1,2,2,1,1,3]))
print(unique_frequency([1,2]))
print(unique_frequency([-3,0,1,-3,1,1,1,-3,10,0]))

# True
# False
# True