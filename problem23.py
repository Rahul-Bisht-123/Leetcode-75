# Equal Row and Column Pairs
'''
Given a 0-indexed n x n integer matrix grid, return the number 
of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain 
the same elements in the same order (i.e., an equal array).


Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]


Example 2:

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

'''

# ------------basic explanations before solution ----------
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
        ]
print(matrix)

# we want to change the rows into columns and columns into rows 
# i.e. transpose     
'''

    c1 c2 c3                     c1 c2 c3
r1  00 01 02    transpose    r1  00 10 20              
r2  10 11 12    =========>   r2  01 11 21                    
r3  20 21 22                 r3  02 12 22
'''

#length of matrix gives total number of 'rows' 
#length of an array in matrix gives number of 'columns'

rows = len(matrix)  #3
cols = len(matrix[0])  #3

print(rows,cols)  #3,3

transpose = []
for i in range(rows):
    transpose.append(list([0,0,0]))

print(transpose)

for r in range(rows):
    for c in range(cols):
        transpose[r][c]=matrix[c][r]
        
print(transpose)

# * = unpack operator
# a,b = [1,2,3,4,5]
# print(a,b)     #ValueError: too many values to unpack (expected 2)
#but when we use unpack operator 
a,*b = [1,2,3,4,5]
print(a,b)  #1 [2, 3, 4, 5]

print('---------------')


# zip = zips together the itertables like (list,tuples..etc) 
# to iterate in all of them at the same time

# it takes first item from each list and zips it together in tuple

a = [1,2,3]
b = ['a','b','c']
for i in zip(a,b):
    print(i)
# (1, 'a')
# (2, 'b')
# (3, 'c')

# ----------
'unpacking the matrix = removing items out from data structures like list or tuples'
print(*matrix)   #[1, 2, 3] [4, 5, 6] [7, 8, 9]

'if we use zip with unpack operator(*)'
'it will take first item each array and makes a tuples of them'

# print(zip(*matrix))   #<zip object at 0x100580700>

for i in zip(*matrix):
    print(i , end = ' ')   #(1, 4, 7) (2, 5, 8) (3, 6, 9)

# ----------------
'now we have to convert this all tuples into list and put them all inside one list'

listing_all_tuples = [list(i) for i in zip(*matrix)]
print(listing_all_tuples)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

'so we got the all matrix rows converted into columns => matrix is transposed'

transpose_matrix_code  = [list(row) for row in zip(*matrix)]
'''
- (*matrix) = unpack or remove the outer data structure like list or tuple 
              and make arrays free
              
- zip(*matrix) = zip them means make a iterable object which will iterate by 
                 taking one-one item from each unpacked array and makes a tuple of it'
                 
- [list(row)] = using list comprehension we are iterating over the iterable tuple objects 
                and converting them into list.

finally we will get a list containing the tranpose of matrix
'''


# -----------------------solution--------

def equal_row_cols(matrix):
    
    #find the tranpose of grid
    transpose = [list(row) for row in zip(*matrix)]
    
    count = 0
    #match each grid item with tranpose items
    for i in matrix:
        for j in transpose:
            if j==i:
                count+=1
    
    return count

print(equal_row_cols([[3,2,1],[1,7,6],[2,7,7]]))  #1

print(equal_row_cols([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))   #3