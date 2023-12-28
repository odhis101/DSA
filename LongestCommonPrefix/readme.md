Problem: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
Example:
For strs = ["flower","flow","flight"], the function should return "fl".
For strs = ["dog","racecar","car"], the function should return "" since there is no common prefix.


my solution 
try looking for matching starting words so i would try split the words in an array and then check if they have the same starting letter if they dont return "" if they do we loop to see where the letter stop being the same and where they do you return the words that were the same for instance fl in the first case 

