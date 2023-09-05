N = int(input())

stack = list()
result = list()

for i in range(N):
    command = input()
    if command == 'size':
        count = 0
        for i in stack:
            if type(i) == type(int()):
                count += 1
        result.append(count)
    elif command == 'pop':
        if not stack:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif command == 'empty':
        if stack:
            result.append(0)
        else:
            result.append(1)
    elif command == 'top':
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
    elif command[0:4] == 'push':
        stack.append(int(command.split()[-1]))

for i in result:
    print(i)