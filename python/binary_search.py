def binary_search(arr, target):
<<<<<<< HEAD
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
=======
    """
    Binary search algorithm to find target in sorted array
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
>>>>>>> upstream/develop
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
<<<<<<< HEAD
    return -1

# Example usage
arr = [1, 2, 4, 7, 9]
target = 7
result = binary_search(arr, target)
print(f"Element found at index: {result}" if result != -1 else "Element not found")
=======
    
    return -1

# Test the function
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in array")
>>>>>>> upstream/develop
