# Delete the Middle Node of a Linked 
'''
You are given the head of a linked list. Delete the middle node, 
and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th 
node from the start using 0-based indexing, where ⌊x⌋ denotes 
the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, 
respectively.
 

Example 1:

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.


Example 3:

Input: head = [2,1]
Output: [2]

Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

'''


# ------------------sol------------
# we are given a linked list having items
# remove the mid element of the link list

# if list len = 1 , mid = 1/2 = 0
# if list len = 2 , mid = 2/2 = 1 
# if list len = 3 , mid = 3/2 = 1
# if list len = 4 , mid = 4/2 = 2
# if list len = 5 , mid = 5/2 = 2
# if list len = 6 , mid = 6/2 = 3
# if list len = 7 , mid = 7/2 = 3


#1->2->3->None
#1->2->3->4->None

def del_middle(head):
    
    if not head.next:       #case for 1 item in list 
        return None
    
    if not head.next.next:   # case for two items in list
        head.next = None
        return head
    
    # handling 3 and 3+ list items
    prev=slow=fast = head
    
    while fast.next and fast.next.next:
        prev=slow
        slow=slow.next
        fast = fast.next.next
    
    if not fast.next:       #fast is at last index , slow is at mid index
        prev.next=slow.next
        return head
    else:                   #fast is at last second index,remove the index next to slow
        slow.next = slow.next.next
        return head           