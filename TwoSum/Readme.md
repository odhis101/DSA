Two Sum:
Problem Statement:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] == 9, so the answer is [0, 1].


simple first solution attempt 


we traverse the array comparing each number and seeing if it will equal the target 9 

function twoSum(nums, target):
    n = length of nums
    for i from 0 to n - 2:
        for j from i + 1 to n - 1:
            if nums[i] + nums[j] equals target:
                return [i, j]

    return []  // No solution found

time complexity of this is 0(n^2)


More Optimal method 

itialization: Create an empty dictionary (num_indices) to store the indices of numbers in the array.

Iterative Process:

For each number in the array (nums), do the following:
Calculate the complement, which is the difference between the target and the current number.
Check if the complement is already in the dictionary (num_indices).
If found, return the indices of the current number and its complement.
If not found, store the current number and its index in the dictionary.

function twoSum(nums, target):
    num_indices = {}  // Dictionary to store the indices of numbers
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return []  // No solution found
