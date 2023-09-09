# Removing Stars From a String
'''
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, 
as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". 
s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". 
s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". 
s becomes "lecoe".

There are no more stars, so we return "lecoe".


Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 
'''

# -----------------sol-------------
# iterate over the s and put its item in list called stack
# if we get a star , remove the last append item in stack using pop()
# if its not a star append it in stack
# finally join the list and return the word

def remove_stars(s):
     stack = []
     
     for i in s:
         if i == '*':
             if stack:
                 stack.pop()
         else:
             stack.append(i)
     
     return ''.join(stack)

print(remove_stars("leet**cod*e"))   #lecoe
    
print(remove_stars("erase*****"))    #''empty string         
             