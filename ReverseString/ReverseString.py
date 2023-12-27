def reverse_string(s):
    return s[::-1]

def reverse_string_complex(s):
    # Initialize an empty string to store the reversed result
    reversed_string = ""

    # Iterate over each character in the original string in reverse order
    for i in range(len(s) - 1, -1, -1):
        # Append the current character to the reversed string
        reversed_string += s[i]

    # Return the reversed string
    return reversed_string

# Test the function
input_str = "hello"
result = reverse_string(input_str)
print(result)


# Test the function
input_str = "hello"
result = reverse_string(input_str)
print(result)
