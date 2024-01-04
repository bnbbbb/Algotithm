import sys

stack = []

for _ in range(int(input())):
    num = sys.stdin.readline().split()
    n = int(num[0])
    
    if n == 1:
        m = int(num[1])
        stack.append(m)
    elif n == 2:
        print(stack.pop() if stack else -1)
    elif n == 3:
        print(len(stack))
    elif n == 4:
        print(0 if stack else 1)
    elif n == 5:
        print(stack[-1] if stack else -1)