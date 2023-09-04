# String Compression
'''
Given an array of characters chars, 
compress it using the following algorithm:

Begin with an empty string s. 
For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, 
but instead, be stored in the input character array chars. 

Note that group lengths that are 10 or longer will be 
split into multiple characters in chars.

After you are done modifying the input array, 
"return the new length of the array."

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".


Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.


Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

'''

# ------------------solution-------
# initialize two varaibles i=first index of current group ,
#                      res = length of compressed string
# 
# while i < len of chars:
#   find the len of current group of consecutive repeating characters (group_len)
#   add char[i] to the answer => char[res]=char[i] , res+=1
#   if group_len>1 , add string representation of group_len ,str(group_len), to the answer
#     ans increase res = res+len(str(group_len))
#   increase i by group_len and proceed to next group

#  Finally return res


def compress(chars):
    i,res = 0,0
    while(i<len(chars)):
        group_len=1
        while(i+group_len<len(chars) and chars[i+group_len]==chars[i]):
            group_len +=1
        chars[res] = chars[i]
        res +=1
        
        if(group_len>1):
            str_repr = str(group_len)
            chars[res:res+len(str_repr)]= list(str_repr)
            res = res+len(str_repr)
        
        i = i+group_len # starting index of new group
    
    return res    
            
print(compress(["a","a","b","b","c","c","c"]))   #6

print(compress(["a"]))  #1

print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))    #4