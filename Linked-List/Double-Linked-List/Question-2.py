# Delete head of DLL
# Easy
# Confident

"""
Given the head of a doubly linked list, remove the node at the head of the linked list and return the head of the modified list.

The head is the first node of the linked list.

#* Example 1
Input: head -> 1 <-> 2 <-> 3

Output: head -> 2 <-> 3

Explanation: The node with value 1 was removed.

#* Example 2
Input: head -> 7

Output: head

Explanation: Note that the head has null value after the removal.

#! Edge cases

- Head is None
- Head is the only node

"""


# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def deleteHead(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return None

        new_head : ListNode = head.next
        new_head.prev = None
        return new_head
