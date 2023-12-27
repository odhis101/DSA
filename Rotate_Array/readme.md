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

