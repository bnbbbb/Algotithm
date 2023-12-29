
import sys

n, m = map(int, sys.stdin.readline().split())
a = set(sys.stdin.readline().split())
b = set(sys.stdin.readline().split())
sum = len(a.difference(b)) + len(b.difference(a))
print(sum)