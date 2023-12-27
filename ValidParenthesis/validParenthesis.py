def isValidParentheses(s):
    def isMatching(left, right):
        return (left == '(' and right == ')') or \
               (left == '{' and right == '}') or \
               (left == '[' and right == ']')

    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-bracket characters from the left
        while left < right and s[left] not in '(){}[]':
            left += 1
        
        # Skip non-bracket characters from the right
        while left < right and s[right] not in '(){}[]':
            right -= 1

        # If both pointers are not on brackets, continue
        if s[left] not in '(){}[]' or s[right] not in '(){}[]':
            left += 1
            right -= 1
            continue
        
        # If the brackets don't match, return False
        if not isMatching(s[left], s[right]):
            return False
        
        left += 1
        right -= 1

    return True

# Test the function
print(isValidParentheses("()"))      # True
print(isValidParentheses("()[]{}"))  # True
print(isValidParentheses("(]"))      # False
print(isValidParentheses("([)]"))    # False
