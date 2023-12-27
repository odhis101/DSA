def rotateArray(nums, k):
    n = len(nums)
    k = k % n

    for i in range(k):
        last_element = nums.pop()
        nums.insert(0, last_element)

# Test the function
nums = [1, 2, 3, 4, 5, 6, 7]
rotateArray(nums, 3)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
