Rotate Array:

Problem: Given an array, rotate the array to the right by k steps, where k is a non-negative integer.
Example: If the array is [1, 2, 3, 4, 5, 6, 7] and k is 3, the rotated array should be [5, 6, 7, 1, 2, 3, 4]

My solution 

i look for k in the array then i remove then i append in into the beginning of the array thus making it looked flipped

here is the psuedo code 

function rotateArray(nums, k):
    n = length(nums)

    # Handle the case where k is larger than the array size
    k = k % n

    # Iterate k times to perform rotation
    for i from 0 to k - 1:
        # Remove the last element
        last_element = nums.pop()

        # Insert the last element at the beginning
        nums.insert(0, last_element)

time complexity 
0(k*n)

However there is a better more effecient way of solving this 

Step 1 (Reverse the Entire Array):

Reverse the entire array. This is equivalent to rotating the array by n positions, where n is the length of the array. The entire array is flipped.
Step 2 (Reverse the First k Elements):

Reverse the first k elements. Now, the first k elements are in their correct rotated positions, and the rest of the array remains flipped.
Step 3 (Reverse the Remaining Elements):

Reverse the remaining elements (from index k to the end). This ensures that the rest of the array is flipped back to its correct order.

function rotateArray(nums, k):
    n = length(nums)

    # Handle the case where k is larger than the array size
    k = k % n

    # Helper function to reverse a portion of the array
    reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Reverse the entire array
    reverse(nums, 0, n - 1)

    # Reverse the first k elements
    reverse(nums, 0, k - 1)

    # Reverse the remaining elements
    reverse(nums, k, n - 1)


