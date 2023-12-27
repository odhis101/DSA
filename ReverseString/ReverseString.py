def reverse_string(s):
    return s[::-1]

def reverse_string_complex(s):
    reversed_string = ""

    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]

    return reversed_string

# Test the function
input_str = "hello"
result = reverse_string(input_str)
print(result)
result1 = reverse_string_complex(result)
print(result1)
