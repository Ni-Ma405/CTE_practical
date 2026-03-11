##Task 1: Implement the List Class Structure 
class CustomList:
    
    def __init__(self):
        self.capacity = 10          # default capacity
        self.size = 0               # current number of elements
        self.data = [None] * self.capacity   # array to store elements
        
        print("Created new CustomList with capacity:", self.capacity)
        print("Current size:", self.size)


# create object
list1 = CustomList()

##Task 2: Implement Basic Operations 
class CustomList:
    
    def __init__(self):
        self.capacity = 10
        self.data = [None] * self.capacity
        self.count = 0

    # 1. append(element)
    def append(self, element):
        self.data[self.count] = element
        self.count += 1
        print("Appended", element, "to the list")

    # 2. get(index)
    def get(self, index):
        print("Element at index", index, ":", self.data[index])

    # 3. set(index, element)
    def set(self, index, element):
        self.data[index] = element
        print("Set element at index", index, "to", element)

    # 4. size()
    def size(self):
        print("Current size:", self.count)


# Example usage
my_list = CustomList()

my_list.append(5)
my_list.get(0)
my_list.set(0, 10)
my_list.get(0)
my_list.size()

