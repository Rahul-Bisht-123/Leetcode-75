# Odd Even Linked List :
'''
Given the head of a singly linked list, group all the nodes 
with odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, 
and so on.

Note that the relative order inside both the even and odd groups 
should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) 
time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]


Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 
'''

# ------------------------sol---------------------

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None
    
        
# [1,2,3,4,5] => [1,3,5,2,4]    
'''
- indexing is starting with odd,even,odd,even....so on
- we will start iteration from the head which will be 1st 
  and at odd index.
- we will use two pointers odd and even , and ehead for ref of even head
- we will connect cur item(odd) next to 

we will convert the 

'''
# [1,2,3,4,5] => [1,3,5,2,4]
def odd_even(head):
    
    if not head:       #0 nodes present
        return None
    
    if not head.next:  #1 node present
        return head
    
    if not head.next.next: #2 nodes present
        return head
    
    #3 and 3+ items case
    odd = head
    even = head.next
    ehead = head.next 
    
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    
    #finally link the odd last node to ehead node
    odd.next = ehead
    
    return head    
        
    
    
    
