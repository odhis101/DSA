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


this is to easy: we can also use a two pointer approach comparing each letter with a pointer both left and right 

Initialize two pointers, one at the beginning of the string (left) and one at the end of the string (right).

While the left pointer is less than the right pointer:

Compare the characters at the left and right positions.
If they are not equal, the string is not a palindrome.
Move the left pointer one step forward and the right pointer one step backward.

function isPalindrome(s):
    // Initialize pointers
    left = 0
    right = length(s) - 1

    // Iterate until left pointer is less than right pointer
    while left < right:
        // Compare characters at left and right positions
        if s[left] is not equal to s[right]:
            return false
        
        // Move pointers towards the center
        left = left + 1
        right = right - 1

    // If the loop completes, the string is a palindrome
    return true
