import sys
n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
n = ''.join(n)
print(n)