games = {'Y': 2, 'F': 3, 'O': 4}

n, g = input().split()

names = set([input() for _ in range(int(n))])

print(len(names)//(games[g]-1))