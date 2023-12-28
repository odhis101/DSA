def threeSum(nums):
    # Edge case: If the array has less than three elements, return an empty list
    if len(nums) < 3:
        return []

    # Sort the array
    nums.sort()

    # Initialize the result list
    result = []

    # Iterate through the array
    for i in range(len(nums) - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Use a dictionary for two-sum-like approach
        seen = set()
        target = -nums[i]

        for j in range(i + 1, len(nums)):
            complement = target - nums[j]
            if complement in seen:
                result.append([nums[i], complement, nums[j]])
                # Skip duplicates to avoid duplicate triplets
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])

    return result


def threeSumOptimal(nums):
    if len(nums) < 3:
        return []

    # Sort the array
    nums.sort()

    result = []
    for i in range(len(nums) - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1

        while left < right:
            # Calculate the current sum
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move the pointers
                left += 1
                right -= 1

            elif current_sum < 0:
                # Increase the sum by moving the left pointer to the right
                left += 1
            else:
                # Decrease the sum by moving the right pointer to the left
                right -= 1

    return result


# Test the function
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(threeSumOptimal(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
