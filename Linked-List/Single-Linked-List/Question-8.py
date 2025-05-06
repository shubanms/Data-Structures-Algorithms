# Insertion at the Kth position of LL
# Easy
# To Revise

'''
Given the head of a singly linked list and two integers X and K, insert a node with value X as the kth node of the linked list and return the head of the modified list.

#* Example 1
Input: head -> 1 -> 2 -> 3, X = 5, K = 2

Output: head -> 1 -> 5 -> 2 -> 3

#* Example 2
Input: head, X = 7, K = 1

Output: head -> 7

Explanation: Note that the value of the head was changed.


#! Edge cases

- The head is None
- k > lenght of the linked list
- k == 1
'''

# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtKthPosition(self, head: ListNode, X: int, K: int):
        node = ListNode(X)
        
        # If the k == 1 then link the new node to the head and return the new node as the new head
        if K == 1:
            node.next = head
            return node
        
        # If there is no head then return None
        if not head:
            return None
        
        # Store the current node the previous node and the count of nodes visited
        curr = head
        prev = None
        cnt = 1

        # Loop through the linked list and check if the current count of the node is equal to the K then insert the new node in between the current node and the previous node
        while curr and cnt != K:
            cnt += 1
            prev = curr
            curr = curr.next

        prev.next = node
        node.next = curr

        return head