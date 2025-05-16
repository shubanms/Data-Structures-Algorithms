# Insert node before (kth node) in DLL
# Easy
# Confident

"""
Given the head of a doubly linked list and two integers X and K, insert a new node with value X, before the Kth node of the linked list and return the head of the modified linked list.

#* Example 1
Input: head -> 1 <-> 3 <-> 5, X = 7, K = 2

Output: head -> 1 <-> 7 <-> 3 <-> 5

Explanation: A node with value 7 was added before the 2nd node.

#* Example 2
Input: head -> 5, X = 7, K = 1

Output: head -> 7 <-> 5

Explanation: A node with value 7 was added, note that the head was changed.

#! Edge cases

- Head is none
- k == 1
- k is out of bounds

"""

# Definition of doubly linked list:


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def insertBeforeKthPosition(self, head: ListNode, X: int, K: int) -> ListNode:
        node = ListNode(X)

        if not head:
            return None

        if K == 1:
            node.next = head
            head.prev = node

            head = node
            return head

        curr = head
        cnt = 1

        while curr and cnt != K:
            curr = curr.next
            cnt += 1

        if not curr:
            return head

        curr.prev.next = node
        node.prev = curr.prev

        curr.prev = node
        node.next = curr

        return head
