#  Asteroid Collision
'''
We are given an array asteroids of integers representing 
asteroids in a row.

For each asteroid, the absolute value represents its size, 
and the sign represents its direction (positive meaning right, 
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. 

-If two asteroids meet, the smaller one will explode. 
-If both are the same size, both will explode. 
-Two asteroids moving in the same direction will never meet.

 
Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. 
The 5 and 10 never collide.


Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. 
The 10 and -5 collide resulting in 10.
 
'''
# --------------sol--------

'''
# Asteriod enters 
    it can be -ve     or      +ve
              /                 \ 
           -ve                   +ve
(<-Its going left)                 (Its going right->)


put ist +ve asteriods in stack 
coz starting -ve asteriods will go left and 
does not harm untill our stack is empty


If -ve asteriod comes then check if
             //                        \\
stack is empty                      stack is not empty
(not to worry,                        (collison can hapen)
it goes out<--)                  (so battle it with +ve item on the top of stack)
                                 (battle till it gets bust or makes stack empty)
'''

def collisons(asteriods):
    stack = []
    
    for i in asteriods:
        if i<0: #-ve =>battle till stack is !empty and top item is big
            while stack and stack[-1]>0:
                top = stack.pop()   #+ve top came out of stack to fight
                if top == abs(i): 
                    #both aesteriods exploded, get out of the while loop
                    break
                elif top>abs(i):
                    #+ve top wins and goes back in stack,and break the while loop
                    stack.append(top)
                    break
                else:
                    #top was low and got killed, so check again for top
                    continue
            
            else: #this will keep the -ve items safe in stack in case no collison happend so that we can return same input array 
                stack.append(i)

            
        else:#+ve
            stack.append(i)
    
    return stack

print(collisons([5,10,-5]))
print(collisons([8,-8]))  
print(collisons([10,2,-5]))   
print(collisons([-2,-1,1,2]))   
            
# [5, 10]
# []
# [10]     
# [-2, -1, 1, 2]      