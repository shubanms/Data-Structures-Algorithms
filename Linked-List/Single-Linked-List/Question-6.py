# Insertion at the head of LL

'''
Given the head of a singly linked list and an integer X, insert a node with value X at the head of the linked list and return the head of the modified list.

The head is the first node of the linked list.

#* Example 1
Input: head -> 1 -> 2 -> 3, X = 7

Output: head -> 7 -> 1 -> 2 -> 3

Explanation: 7 was added as the 1st node.

#* Example 2
Input: head, X = 7

Output: head -> 7

Explanation: 7 was added as the 1st node.


#! Edge cases

- The head is None
'''

# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtHead(self, head: ListNode, X: int):
        node = ListNode(X)
        
        # If there is no head then return the new node
        if not head:
            return node
        
        # Link the new node to the head and return the new node as the new head
        else:
            node.next = head
            return node