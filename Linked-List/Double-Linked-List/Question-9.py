# Insert before given node in DLL
# Easy
# Confident

"""
Given a node's reference within a doubly linked list and an integer X, insert a node with value X before the given node in the linked list while preserving the list's integrity.

You will only be given the node's reference, not the head of the list. It is guaranteed that the given node will not be the head of the list.

#* Example 1
Input: head -> 1 <-> 2 <-> 6, node = 2, X = 7

Output: head -> 1 <-> 7 <-> 2 <-> 6

Explanation: Note that the head was not given to the function.

#* Example 2
Input: head -> 7 <-> 5 <-> 5, node = 5 (node 3), X = 10

Output: head -> 7 <-> 5 <-> 10 <-> 5

Explanation: The last node with value 5 was referenced, thus the new node was added before the last node.


"""

# Definition of doubly linked list:


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def insertBeforeGivenNode(self, node: ListNode, X: int):
        new_node = ListNode(X)

        node.prev.next = new_node
        new_node.prev = node.prev
        new_node.next = node
        node.prev = new_node
