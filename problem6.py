# Reverse Words in a String

'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated 
by a single space.

NOTE: that s may contain leading or trailing spaces or 
multiple spaces between two words. 

The returned string should only have a single 
space separating the words. 
Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain 
leading or trailing spaces.


Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces 
between two words to a single space in the reversed string.

'''

def Reverse_String_Words(string):
    
    #remove the front and back spaces
    #remove the mid extra spaces
    #reverse the string
    #return the string
    str_array = string.split()
    str_array.reverse()
    ans = ' '.join(str_array)
    
    return ans

print(Reverse_String_Words("the sky is blue"))
print(Reverse_String_Words("a good   example"))
print(Reverse_String_Words("  hello world  "))

# blue is sky the
# example good a
# world hello

# ---------------------solution2---------------

def minisolution(string):
    return ' '.join(reversed(string.split()))

print(minisolution('coding is   good   sometimes    '))
# sometimes good is coding

# ---------------sol3----------------

def sol3(string):
    return ' '.join(string.split()[::-1])

print(sol3('   my fish is   swiming   good'))
# good swiming is fish my