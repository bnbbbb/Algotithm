import sys
from collections import deque
n = int(input())
stack = deque()
for _ in range(n):
    n = list(map(int, sys.stdin.readline().split()))
    if n[0] == 1:
        stack.append(n[1])
        stack.rotate(1)
    elif n[0] == 2:
        stack.append(n[1])
    elif n[0] == 3:
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif n[0] == 4:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif n[0] == 5:
        print(len(stack))
    elif n[0] == 6:
        if stack:
            print(0)
        else:
            print(1)
    elif n[0] == 7:
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif n[0] == 8:
        if stack:
            print(stack[-1])
        else:
            print(-1)