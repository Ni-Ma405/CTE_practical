#Task 1: Selection Sort Implementation
def selection_sort(arr):
    # Print the original list
    print("Original list:", arr)

    n = len(arr)

    # Outer loop: goes through each position in the list
    for i in range(n - 1):
        # Assume the current position has the minimum element
        min_index = i

        # Inner loop: find the smallest element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # update index of minimum element

        # Swap the found minimum element with the first element of unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print the list after each pass
        print(f"Pass {i + 1}: {arr}")

    # Print the sorted list
    print("Sorted list:", arr)


# Sample input
arr = [29, 10, 14, 37, 13]

# Function call
selection_sort(arr)

#Task 2: Implement Basic Operations
def selection_sort(arr):
    # Print the original list
    print("Original list:", arr)

    n = len(arr)

    # Variables to count comparisons and swaps
    comparisons = 0
    swaps = 0

    # Outer loop: traverse through the list
    for i in range(n - 1):
        # Assume current index contains minimum element
        min_index = i

        # Inner loop: find the smallest element
        for j in range(i + 1, n):
            comparisons += 1  # Count comparison

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1  # Count swap

        # Print the list after each pass
        print(f"Pass {i + 1}: {arr}")

    # Print the sorted list
    print("Sorted list:", arr)

    # Print total comparisons and swaps
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)


# Sample Input
arr = [29, 10, 14, 37, 13]

# Function Call
selection_sort(arr)

#Task 3: Create an Index Table for Indexed Search
def create_index_table(arr, block_size):
    # Create an empty index table
    index_table = []

    # Traverse the list with step size equal to block size
    for i in range(0, len(arr), block_size):
        # Select the first element of each block
        value = arr[i]

        # Store value and its position as a tuple
        index_table.append((value, i))

    # Display the index table
    print("Index table created:")

    for value, position in index_table:
        print(value, "->", position)


# Sample Input
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
block_size = 3

# Function Call
create_index_table(arr, block_size)
#Task 4: Implement Indexed Search
def indexed_search(arr, index_table, key):
    # Print the search key
    print("Search key:", key)

    # Initialize search range
    imin = 0
    imax = len(arr) - 1

    # Search the index table to determine the possible range
    for i in range(len(index_table) - 1):
        current_value, current_pos = index_table[i]
        next_value, next_pos = index_table[i + 1]

        # Check if key lies between two index values
        if current_value <= key < next_value:
            imin = current_pos
            imax = next_pos - 1

            print("Index range found:")
            print(f"{current_value} <= {key} < {next_value}")
            break

    # If key is greater than or equal to the last index value
    else:
        imin = index_table[-1][1]
        imax = len(arr) - 1

    # Display the search range
    print(f"Searching from index {imin} to index {imax}:")

    # Sequential search inside the selected range
    for i in range(imin, imax + 1):
        print(f"Checking index {i}: {arr[i]}")

        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i

    # Key not found
    print(f"{key} not found")
    return -1


# Sample Input
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

index_table = [
    (10, 0),
    (25, 3),
    (40, 6),
    (55, 9)
]

key = 45

# Function Call
indexed_search(arr, index_table, key)

#Task 5: Test Indexed Search for a Key Not Found
def indexed_search(arr, index_table, key):
    # Print the search key
    print("Search key:", key)

    # Initialize search range
    imin = 0
    imax = len(arr) - 1

    # Search the index table to determine the possible range
    for i in range(len(index_table) - 1):
        current_value, current_pos = index_table[i]
        next_value, next_pos = index_table[i + 1]

        # Check if key lies within the current block range
        if current_value <= key < next_value:
            imin = current_pos
            imax = next_pos - 1

            print("Index range found:")
            print(f"{current_value} <= {key} < {next_value}")
            break

    # If key is greater than or equal to last indexed value
    else:
        imin = index_table[-1][1]
        imax = len(arr) - 1

    # Display the search range
    print(f"Searching from index {imin} to index {imax}:")

    # Sequential search inside selected range
    for i in range(imin, imax + 1):
        print(f"Checking index {i}: {arr[i]}")

        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i

    # Key not found
    print(f"{key} not found")
    return -1


# Sample Input
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

index_table = [
    (10, 0),
    (25, 3),
    (40, 6),
    (55, 9)
]

key = 43

# Function Call
indexed_search(arr, index_table, key)