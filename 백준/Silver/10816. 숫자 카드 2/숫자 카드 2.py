import sys
from collections import Counter
n = int(sys.stdin.readline())
a = list(sys.stdin.readline().split())
c = Counter(a)
m = int(sys.stdin.readline())

result = [c.get(word, 0) for word in sys.stdin.readline().split()]

print(*result)