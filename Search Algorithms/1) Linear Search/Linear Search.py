# Linear Search
# Time Complexity: O(n)

def linear_search(data, target):
    
    for i in range(len(data)):
        if(data[i] == target):
            return i

    return -1


if __name__ == "__main__":
    data = [8, 6, 15, 7, 14]
    target = 7

    result = linear_search(data, target)

    if(result == -1):
        print("Target is not present in the data array")
    else:
        print("Target is present at index", result)