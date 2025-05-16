# Convert Array to DLL
# Easy
# To Revise

"""
Given an array nums, convert it into a doubly linked list and return the head of the list.

#* Example 1
Input: nums = [1, 2, 3, 4]

Output: head -> 1 <-> 2 <-> 3 <-> 4

#* Example 2
Input: nums = [7, 7]

Output: head -> 7 <-> 7

#! Edge cases

- Head is None

"""


# Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def arrayToLinkedList(self, nums: list) -> ListNode:
        if not nums:
            return None

        # Create the head of the linked list
        head = ListNode(val=nums[0])
        curr = head

        # Loop through the elements of the list excluding the first element
        for num in nums[1:]:
            # Create a new node
            node = ListNode(num, prev=curr)

            # Set the current's next to the new node
            curr.next = node

            # Shift and make the new node the current node
            curr = node

        return head
