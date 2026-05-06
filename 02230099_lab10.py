def counting_sort(arr):
    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)

    # Range of the count array
    range_val = max_val - min_val + 1

    # Initialize count array
    count = [0] * range_val

    # Store frequency of each element
    for num in arr:
        count[num - min_val] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(range_val):
        while count[i] > 0:
            sorted_arr.append(i + min_val)
            count[i] -= 1

    return sorted_arr


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))

##part 2
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0–9

    # Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Convert count to cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (stable sorting)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy output back to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find maximum number to know number of digits
    max_val = max(arr)

    # Apply counting sort for each digit place
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr


# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))