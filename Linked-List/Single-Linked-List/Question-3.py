# Deletion of the tail of LL

"""
Given the head of a singly linked list, delete the tail of the linked list and return the head of the modified list.

The tail is the last node of the linked list.

#* Example 1
Input: head -> 1 -> 2 -> 3

Output: head -> 1 -> 2

Explanation: The last node was removed.

#* Example 2
Input: head -> 1

Output: head

Explanation: Note that the value of head is null here.


#! Edge cases

- The head is None
- The head is the only node in the linked list
- The head is the last node in the linked list
"""


# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteTail(self, head: ListNode):
        # Check if head or next node is not None
        if not head or not head.next:
            return None

        current = head

        # Loop through the linked list till we reach node just before the last node
        while current.next.next:
            current = current.next

        # Break the link with the last node and set it to None
        current.next = None

        return head
