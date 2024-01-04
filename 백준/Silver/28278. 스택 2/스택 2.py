import sys
stack = []
for _ in range(int(input())):
    num = sys.stdin.readline().split()
    if len(num) > 1:
        n, m = int(num[0]), int(num[1])
        stack.append(m)
    else:
        n = int(num[0])
        if n == 2:
            if stack:
                print(stack.pop(-1))
            else:
                print(-1)
        elif n == 3:
            print(len(stack))
        elif n == 4:
            if stack:
                print(0)
            else:
                print(1)
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)
            