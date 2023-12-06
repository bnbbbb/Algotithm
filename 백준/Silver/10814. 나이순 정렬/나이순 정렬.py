import sys
n = int(sys.stdin.readline())

join = [sys.stdin.readline().split() for _ in range(n)]
join.sort(key=lambda x :int(x[0]))
for age, name in join:
    sys.stdout.write(f'{int(age)} {name}\n')