# Deletion of the head of LL

"""
Given the head of a singly linked list, delete the head of the linked list and return the head of the modified list.

The head is the first node of the linked list.


#* Example 1
Input: head -> 1 -> 2 -> 3

Output: head -> 2 -> 3

Explanation: The first node was removed.

#* Example 2
Input: head -> 1

Output: head

Explanation: Note that the head of the linked list gets changed.


#! Edge cases

- The head is None 
"""


# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteHead(self, head: ListNode):
        # Check if head is None or the next node is None
        if not head or not head.next:
            return None

        # Else return the next node after the head
        return head.next
