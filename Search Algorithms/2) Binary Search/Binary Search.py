# Binary Search
# Time Complexity: O(log n)
# Stipulation: Data must be sorted.

def binary_search(data, target, high, low):

    if high >= low:
        
        mid = low + (high - low) // 2

        if data[mid] == target:
            return mid

        elif data[mid] > target:
            return binary_search(data, target, mid - 1, low)

        elif data[mid] < target:
            return binary_search(data, target, high, mid + 1)

    return -1

if __name__ == "__main__":
    data = [2, 3, 5, 6, 7, 10]
    target = 7

    result = binary_search(data, target, len(data)-1, 0)

    if(result == -1):
        print("Target is not present in the data array")
    else:
        print("Target is present at index", result)