# Max Consecutive Ones III
'''
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's 
in the array if you can flip at most k 0's.


Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. 
The longest subarray is underlined.


Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]

Bolded numbers were flipped from 0 to 1. 
The longest subarray is underlined.
 
'''
# ----------------sol1---------
# [1,1,1,0,0,0,1,1,1,1,0], k = 2
# given an array of 0's and 1's and a integer k
# we can flip at most k 0's into 1's from array 
# find the largest count of 1's , if k flippings are allowed


# initialize variables i=0 , j=0 in loop , max_len=0 
# now iterate in array from 0 to lastindex using j
# formula to calculate length of 1's => length = j-i+1 (+1 coz its zero based indexing)
# ex: [1,1,1] => if i=0 ,j=2 , len of 1's => j-i+1 = 2-0 +1 = 2+1 =3

# in j loop , check if current item is 0 
# if it is 0 , then reduce the fliping chances => k-=1
# if k goes -ve , then remove items from the starting of window by moving i pointer
# in while loop of k , if item found at i == 0 , then we can increase k
# and till we get +ve k => we have to reduce window => i+=1
# for each iteration of j , compare max_len with cur_len
# max_len = max(max_len,cur_len)
# finally out of the loop , return max_len

def max_consecutive_ones(array,k):
    i=0
    max_len=0
    for j in range(0,len(array)):
        if(array[j]==0):
            k-=1
        while(k<0):
            if array[i]==0:
                k+=1
            i+=1
        cur_len = j-i+1
        max_len=max(max_len,cur_len)
    return max_len

print(max_consecutive_ones([1,1,1,0,0,0,1,1,1,1,0],2))  #6
print(max_consecutive_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))  #10     