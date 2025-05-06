# Deletion of the Kth element of LL

'''
Given the head of a singly linked list and an integer X, delete the node with value X and return the head of the modified list.

#* Example 1
Input: head -> 3 -> 4 -> 5, X = 5

Output: head -> 3 -> 4

Explanation: The node with value 5 was removed.

#* Example 2
Input: head -> 3 -> 4 -> 5, X = 7

Output: head -> 3 -> 4 -> 5

Explanation: No nodes were removed.


#! Edge cases

- The head is None
- The value of the head is the value to remove
- The value is not present in the linked list
'''

# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodeWithValueX(self, head: ListNode, X: int):
        if not head:
            return None

        # If the head val is the target then return the next node in the linked list
        if head.val == X:
            return head.next
        
        # Store the current and the previous node
        curr = head
        prev = None

        # Loop through the linked list and check if the current node value is equal to the target
        while curr:
            # If the node is equal to the target then link the previous to the next node after current, deleting the current node
            if curr.val == X:
                prev.next = curr.next

            # if not found the target then move both the pointers forward
            prev = curr
            curr = curr.next

        return head