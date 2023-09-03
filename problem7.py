# Product of Array Except Self
'''
Given an integer array nums, 
return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums 
is guaranteed to fit in a 32-bit integer.

You must write an algorithm that 
runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


'''
# ------------------------solution1---------TC = O(n^2)-----------
'At each index we need to put product of all remng items except self'
'we can do this using two loops and two variables i and j'
'if i==j then skip it or i!=j then only multiply'

def Product_of_array_except_self(number_array):
    
    ans = []
    for i in range(len(number_array)):
        sum = 1
        for j in range(len(number_array)):
            if i!=j:
                sum *= number_array[j]
        ans.append(sum)
        
    return ans 

print(Product_of_array_except_self([1,2,3,4]))  # [24, 12, 8, 6]
print(Product_of_array_except_self([-1,1,0,-3,3]))  # [0, 0, 9, 0, 0]


# -----------------solution2-------------TC=O(n)--------------SC=O(n)
'we have to create a left product array and right product array'
'that can store the multiplication of left items from current position'
'and multiplication of all the items to the right of it'

# print([1]*4)  [1, 1, 1, 1]

def sol2(number_array):
    length = len(number_array)
    
    #creating left and right product array with all items as 1
    left_product_array = [1]*length    #[1, 1, 1, 1]
    right_prduct_array = [1]*length    #[1, 1, 1, 1]
    
    # now from index 1 to n-1 find the products for left_product arrary
    for i in range(1,length):
         left_product_array[i]=left_product_array[i-1]*number_array[i-1]
         
    #similary from last second index fill the right_product_array
    for i in range(length-2,-1,-1):
        right_prduct_array[i]=right_prduct_array[i+1]*number_array[i+1]
    
    #our cuurent place product ans will be=>product of left*product of right
    ans = []
    for i in range(0,length):
        ans.append(left_product_array[i]*right_prduct_array[i])
    
    return ans

print(sol2([1,2,3,4]))     
print(sol2([-1,1,0,-3,3]))    

# [24, 12, 8, 6]
# [0, 0, 9, 0, 0]


# -----------------sol3-----------TC = O(n)---------SC=O(1)--------

def sol3(nums_array):
    nums_len = len(nums_array)
    ans = [1]*nums_len
    
# we will fill the left product only , in ans array[]
    for i in range(1,nums_len):
        ans[i]=ans[i-1]*nums_array[i-1]
        
# we will get the right product on the go and 
# updating the value of right product as well

    right_product = 1
    for i in range(nums_len-1,-1,-1):
        ans[i] = ans[i]*right_product
        right_product = nums_array[i]*right_product
        
    return ans
        
#given nums =             [1,2,3,4]
#left prod except self  = [1,1,2,6] 
#right prod except self = [24,12,4,1]          

print(sol3([1,2,3,4]))     
print(sol3([-1,1,0,-3,3]))   
# [24, 12, 8, 6]
# [0, 0, 9, 0, 0] 