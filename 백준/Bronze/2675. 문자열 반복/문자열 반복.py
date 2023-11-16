import sys
N = int(sys.stdin.readline())

for _ in range(N):
    x, y = sys.stdin.readline().split()
    sum = ''
    for i in y:
        sum += int(x) * i
    print(sum)