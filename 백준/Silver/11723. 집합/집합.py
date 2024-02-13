
import sys
def solution(n):
    stack_set = set()

    for _ in range(n):
        op = sys.stdin.readline().strip().split()
        if len(op) == 1:
            if op[0] == 'all':
                stack_set = set(range(1, 21))
            elif op[0] == 'empty':
                stack_set = set()
        else:
            operation, x = op[0], int(op[1])
            if operation == 'add':
                stack_set.add(x)
            elif operation == 'remove':
                stack_set.discard(x)
            elif operation == 'check':
                print(1 if x in stack_set else 0)
            elif operation == 'toggle':
                if x in stack_set:
                    stack_set.discard(x)
                else:
                    stack_set.add(x)

n = int(sys.stdin.readline())
solution(n)