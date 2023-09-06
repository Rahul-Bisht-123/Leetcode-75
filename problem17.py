# Longest Subarray of 1's After Deleting One Element
'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing 
only 1's in the resulting array. 
Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, 
[1,1,1] contains 3 numbers with value of 1's.


Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, 
[0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].


Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 
'''

# -------------sol-----------
# initialize start=0,max_len=0,zero_count=0
# iterate over array using the i pointer loop
# if item found is 0 , increase zero_count
# we can afford atmost one zero , coz it will get deleted in end
# if zero count goes above 1 , reduce the window from the start
# window length will be i-start , coz 1 will always be subtracted from total len
# compare len with max_len at each iteration
# finally return the max_len

def longest_subarray_after_deleting_one_element(array):
    start = 0
    max_len = 0
    zero_count = 0
    for i in range(0,len(array)):
        if array[i]==0:
            zero_count+=1
        while(zero_count>1):
            if array[start]==0:
                zero_count-=1
            start+=1
        max_len= max(max_len,i-start)
    
    return max_len


print(longest_subarray_after_deleting_one_element([1,1,0,1]))
#3

print(longest_subarray_after_deleting_one_element([0,1,1,1,0,1,1,0,1]))
#5

print(longest_subarray_after_deleting_one_element([1,1,1]))
#2
