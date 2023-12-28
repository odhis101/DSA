Problem: Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n/2⌋ times. You may assume that the array is non-empty and that the majority element always exists in the array.

here is an Example 

For nums = [3, 3, 4, 2, 4, 4, 2, 4, 4], the majority element is 4.
For nums = [2, 2, 1, 1, 1, 2, 2], the majority element is 2.

this is a simple solution for me what i would do is first try sort the number and have a dictionary with the number and the count of the number as i traverse the array. then i return the key with the highest value 

function majorityElement(nums):
    # Sort the array to group identical numbers together
    sorted_nums = sort(nums)
    
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

this solution is viable but cause of sorting it is done in 0 (n log n ) time 


there is a better solution called Boyer-Moore Voting Algorithm:

he Boyer-Moore Voting Algorithm works by canceling out pairs of elements. The key insight is that if we cancel out an equal number of occurrences of different elements, the majority element (if it exists) will still remain as the majority after the cancellations.

Here's a step-by-step explanation:

Initialization:

We start with a candidate for the majority element and a count initialized to 0.
First Pass - Identify Candidate:

As we traverse the array:
If the count is 0, we set the current element as the candidate.
If the current element is the same as the candidate, we increment the count.
If the current element is different from the candidate, we decrement the count.
The candidate may be the majority element after the first pass.

here is the psuedo code 

function majorityElement(nums):
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
