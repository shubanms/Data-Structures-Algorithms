# Insert node before tail in DLL
# Easy
# To Revise

"""
Given the head of a doubly linked list and an integer X, insert a node with value X before the tail of the linked list and return the head of the modified list.

#* Example 1
Input: head -> 1 <-> 2 <-> 4, X = 3

Output: head -> 1 <-> 2 <-> 3 <-> 4

Explanation: 3 was added before the last node.

#* Example 2
Input: head -> 4, X = 6

Output: head -> 6 <-> 4

Explanation: 6 was added before 4, note that the head was changed as a result.

#! Edge cases

- Head is none
- There is only one node

"""

# Definition of doubly linked list:


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def insertBeforeTail(self, head: ListNode, X: int):
        node = ListNode(X)

        if not head:
            return node

        if not head.next:
            node.next = head
            head.prev = node
            head = node

            return head

        curr = head

        while curr.next:
            curr = curr.next

        node.next = curr
        node.prev = curr.prev

        curr.prev.next = node
        curr.prev = node

        return head
