Problem: Write a function that takes two integers, n and k, and returns the sum of all positive integers less than or equal to n that are multiples of k.
Example: If n = 10 and k = 3, the function should return 18 because the multiples of 3 less than or equal to 10 are 3, 6, and 9, and their sum is 18.


here its simple we want to get the multples of 3 until its less than or equal to 10 

function sumOfMultiples(n, k):
    // Initialize a variable to store the sum
    sum = 0

    // Iterate from k to n
    for i from k to n:
        // Check if i is a multiple of k
        if i is divisible by k:
            // Add i to the sum
            sum = sum + i

    // Return the final sum
    return sum
