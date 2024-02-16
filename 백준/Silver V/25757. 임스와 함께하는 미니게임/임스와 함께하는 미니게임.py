import sys
games = {'Y': 2, 'F': 3, 'O': 4}

n, g = sys.stdin.readline().split()

names = set([sys.stdin.readline() for _ in range(int(n))])

print(len(names)//(games[g]-1))