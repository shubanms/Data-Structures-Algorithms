"""
A doubly linked list is an extension of a singly linked list. 
To fully grasp doubly linked lists, it is essential to understand the concepts of singly linked lists. 

A doubly linked list improves upon the singly linked list by allowing traversal in both directions. 
Each node contains two pointers: one to the next node and one to the previous node. 
This bidirectional nature of the list offers greater flexibility in navigating and modifying the list.

Each node in a doubly linked list stores:
Data: The value of the node.
Next Pointer: The address of the next node.
Back Pointer: The address of the previous node.


Advantages of Doubly Linked Lists:
Bidirectional Traversal: You can traverse the list in both forward and backward directions, which can be helpful for certain operations.
More Efficient Deletion: Deleting a node is more efficient because you have direct access to the previous node, eliminating the need for traversal from the head to find the predecessor.
Insertion Operations: Inserting a node before or after a given node is simpler because you have access to both neighboring nodes.


Disadvantages:
Increased Memory Usage: Each node requires extra memory for the backward pointer, which can be a drawback for memory-constrained environments.
Complexity: The implementation is more complex compared to singly linked lists due to the additional pointer and the need to maintain pointers in both directions.

"""

class Node:
    """ Constructor to initialize a node with data """
    def __init__(self, data):
        # Value of the node
        self.data = data        
        # Pointer to the next node
        self.next = None      
        # Pointer to the previous node
        self.back = None 