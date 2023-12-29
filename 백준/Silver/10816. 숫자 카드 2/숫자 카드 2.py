import sys
from collections import Counter
dic = {}
n = int(sys.stdin.readline())
a = list(sys.stdin.readline().split())
c = Counter(a)
m = int(sys.stdin.readline())
b = list(sys.stdin.readline().split())

for i in b:
    print(c[i], end=" ")