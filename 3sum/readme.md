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


Total time complexity 

Sorting:

The initial sorting of the array has a time complexity of O(n log n), where n is the length of the array.
Nested Loop:

The main nested loop iterates over each element in the array (O(n)).
Within the nested loop, there is a set-based lookup operation and potentially a while loop for skipping duplicates.
In the worst case, the while loop may iterate over all elements, but overall, it does not exceed O(n) iterations.
Total Time Complexity:

The total time complexity is dominated by the sorting step, which is O(n log n).

I am very comfortable with n log n complexity so i might not look for a more optimal solution 

since its a study exercise i had research 

there is a two pointer approach 
Two-Pointer Approach for 3Sum:
Sort the Array:

Start by sorting the array in ascending order. This allows us to efficiently use the two-pointer approach.
Iterate Through the Array:

Use a for loop to iterate through the array.
For each element nums[i], initialize two pointers (left and right) at the next and last elements, respectively.
Check for Duplicates:

Skip duplicate elements for the outer loop to avoid duplicate triplets.
Use Two Pointers:

Move the left pointer forward and the right pointer backward, checking the sum of the three elements (nums[i], nums[left], nums[right]).
Adjust Pointers Based on Sum:

If the sum is equal to zero, add the triplet to the result.
If the sum is less than zero, move the left pointer to the right.
If the sum is greater than zero, move the right pointer to the left.
Skip Duplicates:

While moving the pointers, skip duplicate elements to avoid duplicate triplets.
Return Result:

Return the list of unique triplets.

here is the psuedo code 

function threeSum(nums):
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

        # Initialize two pointers
        left, right = i + 1, len(nums) - 1

        while left < right:
            # Calculate the current sum
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # Add the triplet to the result list
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for both left and right pointers
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
