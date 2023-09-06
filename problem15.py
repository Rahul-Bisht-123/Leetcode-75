# Maximum Number of Vowels in a Substring of Given Length

'''
Given a string s and an integer k, 
return the maximum number of vowel letters 
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.


Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.


Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

'''
# --------------sol1--------TLE
# find the substring of length k
# which has maximum number of vowels

#initialize curvowels = 0
# first find vowels for first k set of elements
# initialize the variable max_vowels = curvowels

# start the sliding window loop
# for each window add one new item , remove one old item
# calculate curvowels
# compare and update max_vowel with curvowels
# finally return max_vowels

def maxVowelsSubstring(str,k):
    cur_vowels = 0
    # str_list = list(str)
    temp_str = []
    for i in range(0,k):
        temp_str.append(str[i])
        if(str[i] in 'aeiou'):
            cur_vowels+=1
            
    max_vowels = cur_vowels
    for i in range(k,len(str)):
        cur_vowels = 0
        temp_str.append(str[i])
        temp_str.pop(0)
        for j in temp_str:
            if j in 'aeiou':
                cur_vowels += 1
                
        if cur_vowels>max_vowels:
            max_vowels=cur_vowels
    
    return max_vowels

print(maxVowelsSubstring("abciiidef",3))  #3
print(maxVowelsSubstring("aeiou",2))      #2
print(maxVowelsSubstring("leetcode",3))   #2    


print('-----------------')        

# ----------------sol2-------------O(n)----------------
# we are given a string s and a length k
# we have to find all the substrings of length k 
# among all these substrings which has the maximum number of vowels
# we have to return that count
# we need to use sliding window here

# s = "abciiidef", k = 3

def max_vowels_substring(s,k):
    cur_vowels = 0
   
    for i in range(0,k):
        if s[i] in 'aeiou':
            cur_vowels +=1
    max_vowels = cur_vowels
    
    for i in range(k,len(s)):
        # cur_vowels = 0
        if s[i] in 'aeiou':
            cur_vowels+=1
        if s[i-k] in 'aeiou':
            cur_vowels-=1
            
        max_vowels=max(max_vowels,cur_vowels)
    
    return max_vowels

print(max_vowels_substring("abciiidef",3))  #3
print(max_vowels_substring("aeiou",2))      #2
print(max_vowels_substring("leetcode",3))   #2   