# Removing given node in DLL
# Easy
# To Revise

"""
Given a node's reference within a doubly linked list, remove that node from the linked list while preserving the list's integrity.

You will only be given the node's reference, not the head of the list. It is guaranteed that the given node will not be the head of the list. For the custom testcase, give the index(0-indexed) of the node to be removed.

#* Example 1
Input: head -> 1 <-> 3 <-> 5, node = 3

Output: head -> 1 <-> 5

Explanation: The referenced node with value 3 was removed.

#* Example 2
Input: head -> 1 <-> 3 <-> 7, node = 7

Output: head -> 1 <-> 3

Explanation: The referenced node with value 7 was removed.

#! Edge cases

- node is the last one
- head is none

"""

# Definition of doubly linked list:


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def deleteGivenNode(self, node: ListNode):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
