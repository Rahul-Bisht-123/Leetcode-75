# Determine if Two Strings are close

'''
Two strings are considered close if you can 
attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb

Operation 2: Transform every occurrence of one existing character 
into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's 
turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, 
return true if word1 and word2 are close, and false otherwise.
 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"


Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.


Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 
'''
# ---------------------basic informations before solution-------
a = {1,2,3,4}
b = {4,3,2,1}
print(type(a),type(b))   #<class 'set'> <class 'set'>

print(a==b)   #True
print(a) #{1, 2, 3, 4}
print(b) #{1, 2, 3, 4}

print('-----------------')

import collections

a = [3,3,3,1,1,1,2,1,1]
freq = collections.Counter(a)

print(freq)    #Counter({1: 5, 3: 3, 2: 1})

print(freq.keys())   #dict_keys([3, 1, 2])

print(freq.values())   #dict_values([3, 5, 1])

print(sorted(freq.values()))   #[1, 3, 5]

print(sorted(freq.keys()))     #[1, 2, 3]
# ----------------------sol-------------------

#both strings should have same length
#both strings should have same identical characters
#both strings freq counters should be same after sorting them

def are_equal_strings(str1,str2):
    if len(str1)!=len(str2):
        return False
    
    if set(str1)!=set(str2):
        return False
    
    str1_counter = collections.Counter(str1)
    str2_counter = collections.Counter(str2)
    
    sorted_values_str1 = sorted(str1_counter.values())
    sorted_values_str2 = sorted(str2_counter.values())
    
    if sorted_values_str1!=sorted_values_str2:
        return False
    
    return True

print(are_equal_strings("abc","bca"))   #True
print(are_equal_strings("a","aa"))     #False
print(are_equal_strings("cabbba", "abbccc"))  #True