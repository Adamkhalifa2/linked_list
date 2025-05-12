# Linked List Implementation

class Node:

    def __init__(self, data):

        self.data = data  # Store the node's value
        self.next = None  # Initialize next pointer to None


class LinkedList:


    def __init__(self):

        self.head = None  # Start with no nodes

    def insert_at_end(self, data):

        # Create a new node with the given data
        new_node = Node(data)

        # If the list is empty, make this the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next

        # Connect the last node to the new node
        current.next = new_node

    def insert_at_start(self, data):

        # Create a new node
        new_node = Node(data)

        # Point the new node to the current head
        new_node.next = self.head

        # Make the new node the new head
        self.head = new_node

    def insert_at_index(self, index, data):

        # Special case: inserting at the start
        if index == 0:
            self.insert_at_start(data)
            return

        # Create the new node
        new_node = Node(data)

        # Find the node just before the insertion point
        current = self.head
        position = 0

        # Traverse to the node just before the desired position
        while current and position < index - 1:
            current = current.next
            position += 1

        # Check if the index is valid
        if current is None:
            raise IndexError("Index out of range")

        # Adjust the links to insert the new node
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):

        # Check if the list is empty
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")

        # Special case: deleting the head
        if index == 0:
            self.head = self.head.next
            return

        # Find the node just before the one to be deleted
        current = self.head
        position = 0

        # Traverse to the node just before the one to be deleted
        while current and position < index - 1:
            current = current.next
            position += 1

        # Check if the index is valid
        if current is None or current.next is None:
            raise IndexError("Index out of range")

        # Remove the node by updating links
        current.next = current.next.next

    def search(self, value):

        # Start from the head of the list
        current = self.head
        index = 0

        # Traverse the list
        while current:
            # Check if current node's data matches the search value
            if current.data == value:
                return index

            # Move to the next node
            current = current.next
            index += 1

        # Value not found
        return -1

    def display(self):
        """
        Print all values in the linked list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Check if the list is empty
        if self.head is None:
            print("Linked list is empty")
            return

        # Traverse and print each node's data
        current = self.head
        while current:
            # Print the data, with an arrow between nodes
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next


# Demonstration of LinkedList functionality
def main():
    """
    Demonstrate the usage of the LinkedList class.
    """
    # Create a new linked list
    ll = LinkedList()

    # Demonstrate insertion methods
    print("Inserting elements:")
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_start(5)
    ll.display()  # Expected: 5 -> 10 -> 20

    # Demonstrate insertion at index
    ll.insert_at_index(1, 7)
    print("\nAfter inserting 7 at index 1:")
    ll.display()  # Expected: 5 -> 7 -> 10 -> 20

    # Demonstrate search functionality
    print("\nSearching for values:")
    print("Index of 10:", ll.search(10))  # Expected: 2
    print("Index of 25:", ll.search(25))  # Expected: -1

    # Demonstrate deletion
    ll.delete_at_index(2)
    print("\nAfter deleting element at index 2:")
    ll.display()  # Expected: 5 -> 7 -> 20


# Only run the main function if this script is run directly
if __name__ == "__main__":
    main()