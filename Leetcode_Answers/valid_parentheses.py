def valid_parentheses(s):
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
    return not stack


print(valid_parentheses("()"))
print(valid_parentheses("()[]{}"))
print(valid_parentheses("(]"))
print(valid_parentheses("([)]"))
print(valid_parentheses("{[]}"))
print(valid_parentheses("(])"))