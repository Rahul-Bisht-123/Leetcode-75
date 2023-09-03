#  Increasing Triplet Subsequence
'''
Given an integer array nums, return true if there 
exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.


Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.


Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
  

'''
'''NOTES: How to assign infinty value to a variable
positive_infinity = float('inf')
negative_infinty = float('-inf')

print(positive_infinity)  #inf
print(negative_infinty)  #-inf

print(float('inf'))  #inf
print(float('-inf')) #-inf

'''
# -----------------solution-----------TC=O(n)------------SC=O(n)
#if we use the brute firce approach and see all sequences
#it will take three loops and TC will be O(n^3)

# but we can do further better,
#steps:
# 1. declare two variables least,second with values as infity
# 2. iterate over the given array=> for i in array
# 3. if current i value is smaller or equal least then update least => least = i
'(if always this above condition is true means array is in decreasing order)'
'and we will get out of the loop and false is returned'

# 4. else if current num is smaller or equal then second ,update second =>second=i
'we found number greater than i'

# 5. else current num is greater than both least and second then => return true
'we found a number greater than both least and second ,i.e. we got the triplet'

#6. if above condtions nothing worked , finally return false

def triplet(array):
    
    first = float('inf')
    second = float('inf')
    
    for i in array:
        if i<=first:first=i
        elif i<=second:second=i
        elif i>=first and i>=second: return True
    
    return False

print(triplet([1,2,3,4,5]))  #True
print(triplet([5,4,3,2,1]))  #False
print(triplet([2,1,5,0,4,6])) #True
print(triplet([1,1,-2,6])) #False



# --------------------sol2-------------TC=O(n)------------SC=O(1)

def triplet2(nums):
    
    if(len(nums)<3):return False  #cannot hapen triplet if values are below 3
    
    first = float('inf')
    second = float('inf')
    
    for i in nums:
        if i<=first:
            first=i
        elif i<=second:
            second=i
        else:     #both above values are found so we are have i>second>first
            return True
    
    #we are out of loop means no above conditions are ful-filled => no triplets
    return False    

print(triplet2([1,2,3,4,5]))  #True
print(triplet2([5,4,3,2,1]))  #False
print(triplet2([2,1,5,0,4,6])) #True
print(triplet2([1,1,-2,6])) #False