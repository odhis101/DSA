I am famialiar with this problem most times you just use 

[::-1]
or something like that

but that is too easy lets try use a loop and store each in an empty string 
function reverseString(s):
    // Initialize an empty string to store the reversed result
    reversedString = ""

    // Iterate over each character in the original string in reverse order
    for i from length(s) - 1 to 0:
        // Append the current character to the reversed string
        reversedString += s[i]

    // Return the reversed string
    return reversedString
