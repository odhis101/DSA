def is_palindrome(s):
    reversed_s = s[::-1]
    return s == reversed_s

# Test the function
input_str = "racecar"
result = is_palindrome(input_str)
print(result)
