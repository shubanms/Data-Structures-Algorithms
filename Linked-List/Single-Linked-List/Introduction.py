"""
A linked list is a linear data structure resembling a chain, where each node is connected to the next,
and each node represents an individual element. Unlike arrays, the elements in a linked list are not stored in contiguous memory locations.

In arrays, adding a new element requires the next memory location to be empty, which cannot always be guaranteed.

Therefore, expanding an array beyond its initial size can be challenging and inefficient.
This limitation is not present in linked lists, which can dynamically grow and shrink as needed.
"""



# Creating a linked list

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def print_linked_list(head: Node) -> None:
    if head is None:
        print("Empty Linked List")
        return  # Exit the function if the list is empty

    curr = head
    linked_list = []

    # Traverse the linked list and collect values
    while curr is not None:
        linked_list.append(str(curr.val))
        curr = curr.next

    # Join the collected values with " -> " and append " -> None"
    print(" -> ".join(linked_list) + " -> None")


# Create a linked list from an array
array = [1, 2, 3, 4, 5]

# Initialize the head of the linked list
head = Node(array[0])
curr = head

# Build the linked list by iterating through the array
for value in array[1:]:
    node = Node(value)
    curr.next = node
    curr = node

# Print the linked list
print_linked_list(head)
