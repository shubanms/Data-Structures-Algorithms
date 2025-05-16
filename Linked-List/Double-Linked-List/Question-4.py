# Delete Kth Element of DLL
# Easy
# To Revise

"""
Given the head of a doubly linked list and an integer k, remove the node at the kth position of the linked list and return the head of the modified list.

#* Example 1
Input: head -> 2 <-> 5 <-> 7 <-> 9, k = 2

Output: head -> 2 <-> 7 <-> 9

Explanation: The node with value 5 was removed.

#* Example 2
Input: head -> 2 <-> 5 <-> 7, k = 1

Output: head -> 5 <-> 7

Explanation: The node with value 2 was removed, note that the head was modified.

#! Edge cases

- k == 1
- k is out of bounds
- head is none

"""

# Definition of doubly linked list:


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def deleteKthElement(self, head: ListNode, k: int):
        if not head:
            return None

        if k == 1:
            if head.next:
                head = head.next
                head.prev = None
            else:
                head = None
            return head

        curr = head
        cnt = 1

        while curr and cnt < k:
            curr = curr.next
            cnt += 1

        if not curr:
            return head

        if curr.prev:
            curr.prev.next = curr.next

        if curr.next:
            curr.next.prev = curr.prev

        return head
