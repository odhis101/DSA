Problem: Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n/2⌋ times. You may assume that the array is non-empty and that the majority element always exists in the array.

here is an Example 

For nums = [3, 3, 4, 2, 4, 4, 2, 4, 4], the majority element is 4.
For nums = [2, 2, 1, 1, 1, 2, 2], the majority element is 2.

this is a simple solution for me what i would do is first try sort the number and have a dictionary with the number and the count of the number as i traverse the array. then i return the key with the highest value 