# Reverse Vowels of String
'''
Given a string s, reverse only all the vowels 
in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', 
and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

'''

# --------------------solution--------------------
# Use two pointers placing at first and last index
# if left and right both poniters are on vowels then swap them
# else left++ and right--

def ReverseVowels(string):
    left = 0
    right = len(string)-1
    
    # convert the string into list to make changes / swap words
    str = list(string)
    vowles = 'aeiouAEIOU'
    
    while (left<right):
        if (str[left] in vowles and str[right] in vowles):
            str[left],str[right] = str[right],str[left]
            left += 1
            right -=1
            
        elif str[left] not in vowles:
            left += 1
            
        elif str[right] not in vowles:
            right -= 1
    
    ans = ''.join(str)
    return ans

print(ReverseVowels('hello'))  #holle
print(ReverseVowels("leetcode")) #leotcede