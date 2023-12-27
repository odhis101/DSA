Palindrome Check:

Problem: Determine if a given string is a palindrome (reads the same backward as forward).
Example: Input: "racecar", Output: True

solution:
this is also easy if you have reversed a string we can easily reverse a string and compare the two words if they are the same return true 

function isPalindrome(s):
    // Reverse the input string
    reversedString = reverseString(s)

    // Check if the original string is equal to the reversed string
    if s equals reversedString:
        return true
    else:
        return false
