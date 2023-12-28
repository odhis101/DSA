Problem: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
Example:
For strs = ["flower","flow","flight"], the function should return "fl".
For strs = ["dog","racecar","car"], the function should return "" since there is no common prefix.


my solution 
try looking for matching starting words so i would try split the words in an array and then check if they have the same starting letter if they dont return "" if they do we loop to see where the letter stop being the same and where they do you return the words that were the same for instance fl in the first case 

function longestCommonPrefix(strs):
    # Edge case: If the array is empty, return an empty string
    if not strs:
        return ""

    # Split the first word into characters
    first_word = list(strs[0])

    # Initialize the result string
    result = ""

    # Iterate over characters in the first word
    for i in range(len(first_word)):
        # Check if the current character is common to all words
        if all(word[i] == first_word[i] for word in strs):
            # Append the character to the result string
            result += first_word[i]
        else:
            # If characters differ, break the loop
            break

    return result
