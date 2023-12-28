import sys
a = sys.stdin.readline().rstrip()
n = set(sys.stdin.readline().split())
a1 = sys.stdin.readline().rstrip()
n1 = sys.stdin.readline().split()
for i in n1:
    if i in n:
        sys.stdout.write('1 ')
    else:
        sys.stdout.write('0 ')