Problem: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


i am familaiar with this problem my prev solution was to use two pointers and to try start from the middle first their should be no middle so if there is a len of 6... you look at the two middle ement numbers and go left and right. this may have been a wrong solution 


here is the pseudo code for this 

function isValidParentheses(s):
    left = 0
    right = length(s) - 1

    while left < right:
        # Skip non-bracket characters from the left
        while left < right and s[left] is not a bracket:
            left += 1
        
        # Skip non-bracket characters from the right
        while left < right and s[right] is not a bracket:
            right -= 1

        # If both pointers are not on brackets, continue
        if s[left] is not a bracket and s[right] is not a bracket:
            left += 1
            right -= 1
            continue
        
        # If the brackets don't match, return False
        if s[left] is not matching bracket for s[right]:
            return False
        
        left += 1
        right -= 1

    return True


This isnt the proper way of doing it, we are to try use stacks 

here is how we do it 

For each character in the string:
If it's an opening bracket ('(', '{', '['), push it onto the stack.
If it's a closing bracket (')', '}', ']'):
Check if the stack is empty. If it is, return False (unmatched closing bracket).
Pop the top element from the stack.
Check if the popped element is the corresponding opening bracket for the current closing bracket. If not, return False (mismatched brackets).


function isValidParentheses(s):
    stack = empty stack

    for char in s:
        if char is an opening bracket ('(', '{', '['):
            push char onto stack
        else if char is a closing bracket (')', '}', ']'):
            if stack is empty:
                return False  // Unmatched closing bracket
            top = pop from stack
            if top is not the corresponding opening bracket for char:
                return False  // Mismatched brackets

    return stack is empty  // True if all opening brackets are matched
