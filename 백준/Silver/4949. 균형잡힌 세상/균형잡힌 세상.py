def is_balanced_string(s):
    stack = []

    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '[' and char != ']'):
                return False

    return not stack

while True:
    input_str = input()
    if input_str == '.':
        break

    result = is_balanced_string(input_str)
    if result:
        print("yes")
    else:
        print("no")
