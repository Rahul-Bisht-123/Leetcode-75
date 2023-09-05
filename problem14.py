# Maximum Average Subarray I
'''
You are given an integer array nums consisting of n elements, 
and an integer k.

Find a contiguous subarray whose length is equal 
to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.


Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''
# ----------------sol------
# we have to find a subarray of size k, whose avg is maximum
# calculate the cursum of first k set items(0,to,k-1)
# initialize variable maxsum=cursum

# making a sliding window loop from i=k to last index
# add one new item from front
# remove one old item from back
# compare maxavg with cur avg

#finally return the value of max avg => maxsum/k

# nums = [1,12,-5,-6,50,3], k = 4

def MaxAvgSubarray(array,k):
    cursum = 0
    for i in range(0,k):#0 to k-1
        cursum += array[i]
        
    maxsum = cursum
    
    #sliding window loop
    for i in range(k,len(array)):#k to last index 
        cursum += array[i]       #add next item
        cursum -= array[i-k]     #remove ist item
        if(cursum>maxsum):       #compairing
            maxsum=cursum
    
    return maxsum/k

print(MaxAvgSubarray([1,12,-5,-6,50,3],4))  #12.75

print(MaxAvgSubarray([5],1))  #5.0