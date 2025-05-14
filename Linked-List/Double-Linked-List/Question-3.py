# Delete Tail of DLL
# Easy
# Confident

"""
Given the head of a doubly linked list, remove the node at the tail of the linked list and return the head of the modified list.

The tail is the last node of the linked list.

#* Example 1
Input: head -> 1 <-> 2 <-> 3

Output: head -> 1 <-> 2

Explanation: The node with value 3 was removed.

#* Example 2
Input: head -> 7

Output: head

Explanation: Note that the head has null value after the removal.

#! Edge cases

- Head is last node
- The linked list is empty

"""


# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def deleteTail(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return None

        curr = head

        while curr.next:
            curr = curr.next

        curr.prev.next = None

        return head
