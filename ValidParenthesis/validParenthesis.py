def isValidParentheses(s):
    stack = []
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_mapping.values():  # Opening bracket
            stack.append(char)
        elif char in bracket_mapping.keys():  # Closing bracket
            if not stack or stack.pop() != bracket_mapping[char]:
                return False  # Mismatched brackets

    return not stack  

# Test the function
print(isValidParentheses("()"))    
print(isValidParentheses("()[]{}"))
print(isValidParentheses("(]"))      
print(isValidParentheses("([)]"))    
