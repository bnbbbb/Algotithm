import sys
a = sys.stdin.readline().rstrip()
for i in range(int(a)):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {num1} + {num2} = {num1 + num2}')