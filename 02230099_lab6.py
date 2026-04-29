def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def median_of_three(low, high):
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]

        # Find median index
        if a <= b <= c or c <= b <= a:
            return mid
        elif b <= a <= c or c <= a <= b:
            return low
        else:
            return high

    def partition(low, high):
        nonlocal comparisons, swaps

        pivot_index = median_of_three(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        swaps += 1

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return arr, comparisons, swaps


# Example usage
data = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comp, swp = quick_sort(data.copy())

print("Original List:", data)
print("Sorted using Quick Sort:", sorted_list)
print("Number of comparisons:", comp)
print("Number of swaps:", swp)

##part2 merge sort
def merge_sort(arr):
    comparisons = 0
    accesses = 0

    if len(arr) <= 1:
        return arr, comparisons, accesses

    def merge(left, right):
        nonlocal comparisons, accesses
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            accesses += 2  # accessing left[i] and right[j]

            if left[i] < right[j]:
                result.append(left[i])
                accesses += 1
                i += 1
            else:
                result.append(right[j])
                accesses += 1
                j += 1

        # remaining elements
        while i < len(left):
            result.append(left[i])
            accesses += 1
            i += 1

        while j < len(right):
            result.append(right[j])
            accesses += 1
            j += 1

        return result

    mid = len(arr) // 2

    left, c1, a1 = merge_sort(arr[:mid])
    right, c2, a2 = merge_sort(arr[mid:])

    comparisons += c1 + c2
    accesses += a1 + a2

    merged = merge(left, right)

    return merged, comparisons, accesses


# Example usage
data = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comp, acc = merge_sort(data)

print("Original List:", data)
print("Sorted using Merge Sort:", sorted_list)
print("Number of comparisons:", comp)
print("Number of array accesses:", acc)