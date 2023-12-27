def compress_string(chars):
    read_ptr = 0
    write_ptr = 0

    while read_ptr < len(chars):
        current_char = chars[read_ptr]
        count = 0

        while read_ptr < len(chars) and chars[read_ptr] == current_char:
            read_ptr += 1
            count += 1

        chars[write_ptr] = current_char
        write_ptr += 1

        if count > 1:
            count_str = str(count)
            for char in count_str:
                chars[write_ptr] = char
                write_ptr += 1

    return write_ptr

# Test the function
input_chars = ["a", "a", "b", "b", "c", "c", "c"]
result_length = compress_string(input_chars)
print(result_length)
print(input_chars[:result_length])  # Modified array
