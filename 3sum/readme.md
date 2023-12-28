problem: Given an array nums of n integers, find all unique triplets in the array that add up to a target sum.
Note:
The solution set must not contain duplicate triplets.
Example:
For nums = [-1, 0, 1, 2, -1, -4] and target = 0, the function should return [[-1, 0, 1], [-1, -1, 2]].

my solution

i have already had a similar problem with the 2 sum i would use the same solution so a dictionary approach i would same the diffrence of two numbers and save them in the dictionary 

Psuedo code to the problem 

function threeSum(nums):
    # Edge case: If the array has less than three elements, return an empty list
    if len(nums) < 3:
        return []

    # Sort the array to simplify the solution
    nums.sort()

    # Initialize the result list
    result = []

    # Iterate through the array
    for i in range(len(nums) - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Set the target sum to the negation of the current element
        target_sum = -nums[i]

        # Use a dictionary to find pairs that sum to the target
        seen = set()
        for j in range(i + 1, len(nums)):
            complement = target_sum - nums[j]
            if complement in seen:
                # Add the triplet to the result list
                result.append([nums[i], complement, nums[j]])
                # Skip duplicates to avoid duplicate triplets
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])

    return result
