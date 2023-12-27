Problem: Given a string consisting of lowercase English letters, compress it in-place. The length after compression must always be smaller than or equal to the original string. If the compressed string is longer than the original string, your function should return the original string.

Input: ["a", "a", "b", "b", "c", "c", "c"]
Output: Return 6 and modify the input array to ["a", "2", "b", "2", "c", "3"]
Input: ["a"]
Output: Return 1 and modify the input array to ["a"]
Input: ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
Output: Return 4 and modify the input array to ["a", "b", "1", "2"]

my solution is to have two pointers one looking at the index with the new letter and counting through it. i am assuming that the letters are organized 

function compressString(chars):
    read_ptr = 0
    write_ptr = 0

    while read_ptr < length(chars):
        current_char = chars[read_ptr]
        count = 0

        while read_ptr < length(chars) and chars[read_ptr] == current_char:
            read_ptr += 1
            count += 1

        chars[write_ptr] = current_char
        write_ptr += 1

        if count > 1:
            count_str = convertCountToString(count)
            for char in count_str:
                chars[write_ptr] = char
                write_ptr += 1

    return write_ptr


    this solution is in 0(1) time 
