# Traversal in Linked List

"""
Given the head of a singly Linked List. Traverse the entire Linked List and return its elements in an array in the order of their appearance.


#* Example 1
Input: head -> 5 -> 4 -> 3 -> 1 -> 0

Output: [5, 4, 3, 1, 0]

Explanation: The nodes in the Linked List are 5 -> 4 -> 3 -> 1 -> 0, with the head pointing to node with value 5.

#* Example 2
Input: head -> 1

Output: [1]

Explanation: Only one node present in the list.

"""


# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def LLTraversal(self, head: ListNode):
        # Check if head is None
        if not head:
            return None

        linked_list = []

        curr = head

        # Loop through nodes and store the value of each node in a list
        while curr:
            linked_list.append(curr.val)

            # Move to the next node
            cur = cur.next

        return linked_list
