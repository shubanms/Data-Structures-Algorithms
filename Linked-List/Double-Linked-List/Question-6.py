# Insert node before head in DLL
# Easy
# Confident

"""
Given the head of a doubly linked list and an integer X, insert a node with value X before the head of the linked list and return the head of the modified list.

#* Example 1
Input: head -> 1 <-> 2 <-> 3, X = 3

Output: head -> 3 <-> 1 <-> 2 <-> 3

Explanation: 3 was added before the 1st node. Note that the head's value is changed.

#* Example 2
Input: head -> 5, X = 7

Output: head -> 7 <-> 5

#! Edge cases

- there is no head

"""

# Definition of doubly linked list:


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def insertBeforeHead(self, head: ListNode, X: int):
        node = ListNode(X)

        if not head:
            head = node
            return head

        node.next = head
        head.prev = node

        head = node

        return head
