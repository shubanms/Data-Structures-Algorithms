# Insertion before the value X in LL

'''
Given the head of a singly linked list and two integers X and val, 
insert a node with value val before the node with value X in the linked list and return the head of the modified list.

#* Example 1
Input: head -> 1 -> 2 -> 3, X = 2, val = 5

Output: head -> 1 -> 5 -> 2 -> 3

Explanation: The node with value 5 was added before the node with value 2

#* Example 2
Input: head -> 1 -> 2 -> 3, X = 7, val = 5

Output: head -> 1 -> 2 -> 3

Explanation: No node was added as X was not found in the list.


#! Edge cases

- The head is None
- X does not exist
- X is the first node
- X is the last node
'''

# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertBeforeX(self, head: ListNode, X: int, val: int):
        node = ListNode(val)
        
        if not head:
            return None
        
        # If the head value is equal to the target then link the new node to the head and return the new node as the new head
        if head.val == X:
            node.next = head
            return node
        
        curr = head
        prev = None

        # Loop through the linked list till we find the target and when we find it then insert the new node in between the current node and the previous node
        while curr:
            if curr.val == X:
                prev.next = node
                node.next = curr
                break
            prev = curr
            curr = curr.next

        return head