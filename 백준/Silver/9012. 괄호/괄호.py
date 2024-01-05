n = int(input())

def check(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return stack == []

for _ in range(n):
    string = input()
    if check(string):
        print('YES')
    else:
        print('NO')