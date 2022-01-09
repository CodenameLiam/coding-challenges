# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isValid(s: str) -> bool:
    # Base case
    if s[0] in {")","}","]"} or len(s)==1:
        return False

    # Data structures
    stack = []
    map =  { "}":"{" , "]":"[" , ")":"("}

    # For each char...
    for char in s:
        # Add it to the stack if it's an opening parenthesis
        if char in map.values():
            stack.append(char)
        # If it's a closing parenthesis, and nothing is on the stack, the string is not valid
        # If it's a closing parenthesis, and the stack does not contain the opening parenthesis, the string is not valid
        elif char in map.keys():
            if stack == [] or map[char] != stack.pop():
                return False
        # If the character is not some reason not a parenthesis, the string is not valid
        else:
            return False

    # Because we pop the stack when comparing parentheses, the string will be valid if the stack is empty
    return stack == []



print(isValid("()[]{}"))