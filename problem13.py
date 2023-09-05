# Max Number of K-Sum Pairs
'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the 
array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 
Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.


Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 
'''
# ---------------sol1-------
# sort the array
# Use count and put pointers at i=start and j=end
# cal sum => sum =i+j
# if sum == k , then increase count , and move pointers i++,j--
# else if sum<k , i++
# else if sum >k, j--
# finally return count

def ksum_pairs(array,k):
    i=0
    j=len(array)-1
    ans = 0
    array.sort()
    while(i<j):
        sum=array[i]+array[j]
        if(sum==k):
            ans+=1
            i+=1
            j-=1
        elif(sum<k):
            i+=1
        elif(sum>k):
            j-=1
    return ans

print(ksum_pairs([1,2,3,4],5))   #2
print(ksum_pairs([3,1,3,4,3], 6))   #1
