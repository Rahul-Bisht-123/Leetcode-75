# Greatest common divisor of strings

'''
For two strings s and t, we say "t divides s" 
if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, 
return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
# ----------------
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
# -------------------

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


'''
# --------------------solution-------------------

#check if str1+str2 == str2+str1
#if they are not equal then return empty string

#if they are equal then calculate gcd of both string lengths
#and return that much slice from the string

import math
def gcd_strings(str1,str2):
    
    if(str1+str2 != str2+str1):
        return "no gcd"
    
    max_len = math.gcd(len(str1),len(str2))
    
    return str1[:max_len]

print(gcd_strings("ABCABC","ABC"))  #ex1
print(gcd_strings("ABABAB","ABAB")) #ex2
print(gcd_strings("LEET","CODE"))  #ex3

# ABC
# AB
# no gcd