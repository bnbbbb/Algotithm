n, m = map(int, input().split())

fruits = list(map(int, input().split()))
fruits.sort()
for fruit in fruits:
    if m >= fruit:
        m += 1

print(m)