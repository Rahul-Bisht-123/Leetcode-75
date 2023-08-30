# ------------------Merge Strings Alternatively------------------'

'''
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, 
starting with word1. 

If a string is longer than the other, 
append the additional letters onto the 
end of the merged string.

# Return the merged string.
'''

'''
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

'''
# -----------------------_Solution_1-----------------------------
# we are given two strings a,b
# merge the strings alternatively

a = 'ab'
b = 'pqrs'
output = 'apbqrs'

'step1 : make the string into characters of list'
# -----------
list_a = list(a)   #tyepcast to list
list_b = list(b)   #tpecast to list

# print(list_a)  ['a', 'b']
# print(list_b)  ['p', 'q', 'r', 's']

'step2 : loop over the two strings using while loop '
'and add alternative items'

len1 = len(a)
len2 = len(b)

# print(len1,len2)  #2, 4

i,j=0,0
ans = ''
while(i<len1 and j<len2):
    ans = ans + list_a[i]
    ans = ans + list_b[j]
    i=i+1
    j=j+1
    
# print(ans)  apbq

'step3 : append all the pending items from the while loop break'

while(i<len1):
    ans=ans+list_a[i]
    i=i+1

while(j<len2):
    ans = ans+list_b[j]
    j+=1
    
print('Sol1 = ',ans)   #apbqrs  

# -------------------------Solution 2---------------------
'Using one while loop'
def solution2(word1,word2):
    
    ans = ''
    i,j = 0,0
    while(i<len(word1) or j<len(word2)):
        
        if(i<len(word1)):
            ans = ans + word1[i]
            i+=1
        if(j<len(word2)):
            ans = ans +word2[j]
            j+=1
    
    return ans

print('sol2 = ',solution2(a,b))
# sol2 =  apbqrs

# ----------------------Solution3------------------------------  
'Using one pointer'

'NOTE:max() returns greatest value from list of iterables'

def sol3(word1,word2):
    ans = ''
    maxlen = max(len(word1),len(word2))
    for i in range(maxlen):
        if(i<len(word1)):ans=ans+word1[i]
        
        if(i<len(word2)):ans=ans+word2[i]

            
    return ans

print('sol3 = ',sol3(a,b))
# sol3 =  apbqrs