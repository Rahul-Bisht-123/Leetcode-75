# Is Subsequence
'''
Given two strings s and t, return true 
if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string 
that is formed from the original string by 
deleting some (can be none) of the characters 
without disturbing the relative positions of 
the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true


Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

'''

# -----------------sol1--------
# Check if subsequence is empty , if yes return true
# initiate a variable , subseq_idx , which is indexes for subsequence
# iterate over the word from start to end 
# match all occurences of subsequence letters with word letters
# if match happens => increment the subseq_idx
# if increment_idx , becomes equal to len (word), return true

# finally loop ends and nothing is returned then
# return false


def IsSubsequence(s,t):
    
    if not s:
        return True
    
    subseq_idx = 0
    
    for i in t:
        if i==s[subseq_idx]:
            subseq_idx +=1
            
        if(subseq_idx==len(s)):
            return True
    
    return False    
    
print(IsSubsequence("abc","ahbgdc"))   #True
print(IsSubsequence("axc","ahbgdc"))   #False