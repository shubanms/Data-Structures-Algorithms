# Insertion at the tail of LL
# Easy
# Confident

'''
Given the head of a singly linked list and an integer X, insert a node with value X at the tail of the linked list and return the head of the modified list.

The tail is the last node of the linked list.

#* Example 1
Input: head -> 1 -> 2 -> 3, X = 7

Output: head -> 1 -> 2 -> 3 -> 7

Explanation: 7 was added as the last node.

#* Example 2
Input: head, X = 0

Output: head -> 0

Explanation: 0 was added as the last/only node.


#! Edge cases

- The head is None
'''

# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtTail(self, head: ListNode, X: int):
        node = ListNode(X)
        # If the head is None return None
        if not head:
            return node
        
        curr = head

        # Loop through the linked list till we get to the last node 
        while curr.next:
            curr = curr.next

        # Link the last node to the new created node and the new created node to link to None
        curr.next = node

        return head