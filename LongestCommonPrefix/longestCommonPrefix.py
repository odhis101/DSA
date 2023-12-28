def longestCommonPrefix(strs):
    # Edge case: If the array is empty, return an empty string
    if not strs:
        return ""

    # Split the first word into characters
    first_word = list(strs[0])

    # Initialize the result string
    result = ""

    # Iterate over characters in the first word
    for i in range(len(first_word)):
        # Check if the current character is common to all words
        if all(word[i] == first_word[i] for word in strs):
            result += first_word[i]
        else:
            break

    return result
def longestCommonPrefixOptimized(strs):
    # Edge case: If the array is empty, return an empty string
    if not strs:
        return ""

    # Use zip to group characters from the same position together
    for i, group in enumerate(zip(*strs)):
        # Check if all characters in the group are the same
        if len(set(group)) == 1:
            continue
        else:
            # If a mismatch is found, return the common prefix up to this point
            return strs[0][:i]

    # If no mismatch is found, return the entire first word as the common prefix
    return strs[0]

# Test the function



# Test the function
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]

print(longestCommonPrefix(strs1))  # Output: "fl"
print(longestCommonPrefix(strs2))  # Output: ""

print(longestCommonPrefixOptimized(strs1))  # Output: "fl"
print(longestCommonPrefixOptimized(strs2))  # Output: ""