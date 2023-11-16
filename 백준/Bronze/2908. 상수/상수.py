import sys
x, y = sys.stdin.readline().split()
if int(x[::-1]) > int(y[::-1]):
    print(int(x[::-1]))
else:
    print(int(y[::-1]))