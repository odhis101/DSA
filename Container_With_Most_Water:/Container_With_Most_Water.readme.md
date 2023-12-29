Problem: Given an array of non-negative integers height, where each element represents the height of a vertical line, determine the maximum area that can be formed between two vertical lines by selecting two indices.

Function Signature: def max_area(height: List[int]) -> int

height = [1,8,6,2,5,4,8,3,7]
max_area(height)  # Output: 49

Container With Most Water:
You are given an array height where each element represents the height of a vertical line.
The indices of the array represent positions along a line.
The goal is to find two vertical lines (at different indices) that together with the x-axis forms a container that can hold the most water.
Example:
Consider the array height = [1,8,6,2,5,4,8,3,7]. Each element of the array represents the height of a vertical line at a specific position:


   #
   #               #
   #               #     #
   #     #         #     #  #
   #     #     #   #     #  #
   #     #     #   #  #  #  #
   #     #  #  #   #  #  #  #
   #  #  #  #  #   #  #  #  #
   ---------------------------
   1  8  6  2  5  4  8  3  7
