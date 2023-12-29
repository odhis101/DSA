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


this problem was difficult for me to undestand so i just googled and youtubed the solution 

Approach Summary:
Two-Pointer Technique:

Initialize two pointers, left at the beginning and right at the end of the array.
The idea is to explore different pairs of lines by moving the pointers towards each other.
At each step, calculate the width (distance between the lines) and the container height (minimum height of the two lines).
Calculate the area of the container using the formula area = width * container_height.
Update a variable max_area to track the maximum area encountered.
Move the pointers towards each other based on the logic of minimizing height while maximizing width.