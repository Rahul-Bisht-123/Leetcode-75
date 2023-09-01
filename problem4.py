# Can Place Flowers
'''
You have a long flowerbed in which some of 
the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed
containing 0's and 1's, where 0 means 
empty and 1 means not empty, and an 
integer n, return true if n new flowers 
can be planted in the flowerbed without 
violating the no-adjacent-flowers rule 
and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

'''
# ------------------------solution------------------
# traverse over the array and find the places which have zero
# for each zero place check if its right and left places are empty
# if they are both empty we can put a flower there ,and set it to 1
# and increase the count variable

def PlantFlower(flower,n):
    
    count = 0 
    #loop over the array to find 0 places
    for i in range(len(flower)):
        if flower[i]==0:
            left_empty  = (flower[i-1]==0) or (i==0)
            right_empty = (flower[i+1]==0) or (i==len(flower)-1)
            
        #if both places are empty put a 1 or flower there
            if left_empty and right_empty: 
                flower[i]=1
                count+=1
            
    return count>=n

print(PlantFlower([1,0,0,0,1],1))
print(PlantFlower([1,0,0,0,1],2))

# True
# False
            
            
# -------------------------solution2-----------------
#instead of counting count till last value
#we can put a check condition thta if count>=n retunr true

def plant_flower(flowerbed,n):
    
    count=0
    for i in range(len(flowerbed)):
        if flowerbed[i]==0:
            left_empty = (i==0) or (flowerbed[i-1]==0)
            right_empty = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
            
            if(left_empty and right_empty):
                flowerbed[i]=1
                count+=1
                if(count>=n):return True
    
    return count>=n
        
print(plant_flower([1,0,0,0,1],1))
print(plant_flower([1,0,0,0,1],2))    

# True
# False