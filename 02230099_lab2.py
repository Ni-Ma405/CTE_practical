# Node class
class Node:
    def __init__(self, data):
        self.data = data      # store element
        self.next = None      # reference to next node


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None      # first node
        self.tail = None      # last node
        self._size = 0        # size counter

        print("Created new LinkedList")
        print("Current size:", self._size)
        print("Head:", self.head)
        
        # Append (add at end)
    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(f"Appended {element} to the list")

    # Get element by index
    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next

        print(f"Element at index {index}: {current.data}")
        return current.data

    # Set element at index
    def set(self, index, element):
        current = self.head
        for i in range(index):
            current = current.next

        current.data = element
        print(f"Set element at index {index} to {element}")

    # Return size
    def size(self):
        print("Current size:", self._size)
        return self._size

    # Prepend (add at beginning)
    def prepend(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self._size += 1
        print(f"Prepend {element} to the list")

    # Print list
    def print_list(self):
        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print("Print Linked list: [" + " ".join(elements) + "]")
        
# Create list
ll = LinkedList()

# Operations
ll.append(5)
ll.get(0)
ll.set(0, 10)
ll.get(0)
ll.size()
ll.prepend(10)
ll.print_list()