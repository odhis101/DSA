def rotateArray(nums, k):
    n = len(nums)
    k = k % n

    # Helper function to reverse a portion of the array
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)

    # Reverse the remaining elements
    reverse(nums, k, n - 1)

# Test the function
nums = [1, 2, 3, 4, 5, 6, 7]
rotateArray(nums, 3)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
