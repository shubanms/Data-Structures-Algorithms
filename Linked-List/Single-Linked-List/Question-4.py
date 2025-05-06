# Deletion of the Kth element of LL
# Easy
# To Revise

'''
Given the head of a singly linked list and an integer k, delete the kth node of the linked list and return the head of the modified list.

#* Example 1
Input: head -> 3 -> 4 -> 5, k = 2

Output: head -> 3 -> 5

Explanation: The 2nd node with value 4 was removed.

#* Example 2
Input: head -> 1 -> 2 -> 3, k = 1

Output: head -> 2 -> 3

Explanation: The 1st Node was removed, note that the value of the head has changed.


#! Edge cases

- The head is None
- The head is the only node in the linked list
- The head is the kth node in the linked list
- The kth node is the last node in the linked list
- The kth node is not present in the linked list
'''


# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteKthNode(self, head: ListNode, k: int):
        # If head is not present return None
        if not head:
            return None

        # If we have to delete the first node return the next node after head
        if k == 1:
            return head.next

        # Keep track of the current node the previous node and the count of nodes we have visited
        curr = head
        prev = None
        cnt = 1

        # Loop through the linked list while the current node is valid and the count is less than k
        while curr and cnt != k:
            prev = curr
            curr = curr.next
            cnt += 1

        # Skip the kth node 
        prev.next = curr.next

        return head