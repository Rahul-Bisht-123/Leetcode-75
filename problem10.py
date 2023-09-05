# Move Zeroes

'''
Given an integer array nums, move all 0's to 
the end of it while maintaining the relative 
order of the non-zero elements.

Note that you must do this in-place 
without making a copy of the array.

 
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]


Example 2:

Input: nums = [0]
Output: [0]

'''

# -----------------sol1-----using two extra arrays

def move_zeros(nums):
    array_0 = []
    array_1 = []
    
    for i in nums:
        if i!=0:
            array_1.append(i)
        else:
            array_0.append(i)
    
    nums = []
    nums = array_1+array_0
    print(nums)

move_zeros([0,1,0,3,12])
# [1, 3, 12, 0, 0]

# ----------------------------sol2-------without extra space----

def move_zeros2(nums):
    
    #move all the non zero items in start of list
    writing_index = 0
    
    for i in nums:
        if i!=0:
            nums[writing_index]=i
            writing_index += 1
    
    # all extra zeros in the last acc to array pending size
    while(writing_index<len(nums)):
        nums[writing_index] = 0
        writing_index +=1
    
    return nums
      
print(move_zeros2([0,1,0,3,12]))
# [1, 3, 12, 0, 0]