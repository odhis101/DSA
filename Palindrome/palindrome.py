def is_palindrome(s):
    reversed_s = s[::-1]
    return s == reversed_s

def is_palindrome_complex(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Compare characters at left and right positions
        if s[left] != s[right]:
            return False

        # Move pointers towards the center
        left += 1
        right -= 1

    # If the loop completes, the string is a palindrome
    return True

# Test the function
input_str = "level"
result = is_palindrome(input_str)
print(result)

result1 = is_palindrome_complex(input_str)
print(result1)

