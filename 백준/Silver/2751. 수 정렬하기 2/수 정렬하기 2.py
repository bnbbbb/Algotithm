import sys
a = []
b = int(sys.stdin.readline())
for _ in range(b):
    a.append(int(sys.stdin.readline()))

a.sort()
for i in a:
    print(i)