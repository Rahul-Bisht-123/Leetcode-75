# Reverse Linked List

'''
Given the head of a singly linked list, 
reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

'''
# -------------sol--------
# [1,2,3,4,5->none] => [5,4,3,2,1->None]

# we will use three pointers prev cur nxt


def revLinkedList(head):
    prev = None
    cur = head
    
    while cur:
        nxt = cur.next
        #save the cur.next for last using for each iteration
        
        cur.next=prev
        #make each current node points to its prev
        
        #move the prev to cur and cur to cur.next (basically one step ahead)
        prev = cur
        cur = nxt
 
# in the end cur is on none and the prev will be on last node, so return the prev    
    return cur