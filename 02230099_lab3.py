class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * capacity  # underlying array
        self.top = -1  # indicates empty stack
        print(f"Created new ArrayStack with capacity: {capacity}")
        print(f"Stack is empty: {self.is_empty()}")

    # Push operation
    def push(self, element):
        if self.top == self.capacity - 1:
            print("Stack Overflow! Cannot push element.")
            return
        self.top += 1
        self.stack[self.top] = element
        print(f"Pushed {element} to the stack")

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        element = self.stack[self.top]
        self.top -= 1
        print(f"Popped element: {element}")
        return element

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        print(f"Top element: {self.stack[self.top]}")
        return self.stack[self.top]

    # Check if stack is empty
    def is_empty(self):
        return self.top == -1

    # Size of stack
    def size(self):
        return self.top + 1

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Display stack:", self.stack[:self.top + 1])
            
            # Create stack
s = ArrayStack(10)

# Operations
s.push(10)
s.display()

s.push(20)
s.display()

s.push(30)
s.display()

s.peek()

s.pop()

print("Stack size:", s.size())
s.display()