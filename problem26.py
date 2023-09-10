# Decode String
'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], 
where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is 
guaranteed to be a positive integer.

You may assume that the input string is always valid; 
there are no extra white spaces, square brackets are 
well-formed, etc. Furthermore, you may assume that the 
original data does not contain any digits and that digits 
are only for those repeat numbers, k. 

For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the 
output will never exceed 105.
 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"


Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"


Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 
'''
a = '3'
# print(a.isnumeric())   #True


# -------------------sol---------------------
# We are given a string which have => number , characters , square brackets[ ]
# eg = 3[a]2[bc]

#we have to copy the bracket inside string according to the number at its starting square bracket
# 3[a] = aaa
#2[bc] = bcbc

# we also have nested brackets
# 3[a2[c]] = 3[acc] = accaccacc



# -------------------------code1----------------
# 3[a]2[bc]
# 3[a2[c]]
def decode(encoded_string):
    stack = []
    
    for i in encoded_string:
        if i!=']':
            stack.append(i)
            
        else:#do the decoding and append it back to stack
            
            s = ''
            while stack and stack[-1]!='[':
                s = stack.pop() + s
                #the pop will be in rev order so we adding s in end not in start
                
            if stack[-1]=='[':
                stack.pop()  #open bracket removed
            
            num = ''
            while stack and stack[-1].isnumeric():
                num = stack.pop() + num     
                #this pop will be in rev order so we add num at end not in start
            
            stack.append(s*int(num))
    
    return ''.join(stack)
    
print(decode('2[abc]3[cd]ef'))
print(decode('3[a2[c]]'))  
print(decode('3[a]2[bc]'))          

# abcabccdcdcdef
# accaccacc
# aaabcbc