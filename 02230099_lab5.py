def sequential_search(arr, target):
    comparisons = 0
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons   # return index and comparisons
    
    return -1, comparisons   # if not found


# Example usage
arr = [23, 45, 12, 67, 89, 34, 56]
target = 67

index, comparisons = sequential_search(arr, target)

print("List:", arr)
print("Searching for", target, "using Sequential Search")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)

##Part 2
# Binary Search Implementation (Iterative and Recursive)

# Iterative Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# Recursive Binary Search
def binary_search_recursive(arr, target, low, high, comparisons=0):
    if low > high:
        return -1, comparisons

    mid = (low + high) // 2
    comparisons += 1

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)


# Example Usage
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67

print("Sorted List:", arr)
print("Searching for", target, "using Binary Search")

# Iterative Result
index, comparisons = binary_search(arr, target)

if index != -1:
    print("\nIterative Binary Search:")
    print("Found at index", index)
else:
    print("\nIterative Binary Search:")
    print("Not found")

print("Number of comparisons:", comparisons)

# Recursive Result
index_r, comparisons_r = binary_search_recursive(arr, target, 0, len(arr) - 1)

if index_r != -1:
    print("\nRecursive Binary Search:")
    print("Found at index", index_r)
else:
    print("\nRecursive Binary Search:")
    print("Not found")

print("Number of comparisons:", comparisons_r)