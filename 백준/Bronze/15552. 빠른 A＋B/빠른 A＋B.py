import sys
a = sys.stdin.readline().rstrip()
for _ in range(int(a)):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(num1 + num2)