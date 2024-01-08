from collections import deque
import sys
n = int(sys.stdin.readline())
stack = deque()

for _ in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        print(stack.popleft()) if stack else print(-1)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        print(0) if stack else print(1)
    elif a[0] == 'front':
        print(stack[0]) if stack else print(-1)
    elif a[0] == 'back':
        print(stack[-1]) if stack else print(-1)