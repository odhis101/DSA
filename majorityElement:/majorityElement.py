def majorityElement(nums):
    # Sort the array to group identical numbers together
    sorted_nums = sorted(nums)
    
    # Initialize a dictionary to store the count of each number
    count_dict = {}

    # Traverse the sorted array and count occurrences
    for num in sorted_nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the key with the maximum value in the dictionary
    majority_element = max(count_dict, key=count_dict.get)

    return majority_element
def majorityElement_effecient(nums):
    candidate = None
    count = 0

    # First pass: Find a potential majority element
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Second pass: Verify if the candidate is the majority element
    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    # Check if the candidate is the majority element
    return candidate if count > len(nums) // 2 else None
# Test the function
nums1 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
nums2 = [2, 2, 1, 1, 1, 2, 2]

print(majorityElement(nums1))  # Output: 4
print(majorityElement(nums2))  # Output: 2

print(majorityElement_effecient(nums1))  # Output: 4   
print(majorityElement_effecient(nums2))  # Output: 2
