import sys
a = int(input())
b = list(map(int, sys.stdin.readline().split()))
c = int(input())
print(b.count(c))