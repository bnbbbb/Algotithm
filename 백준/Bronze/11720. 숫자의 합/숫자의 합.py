a = int(input())
b = list(input())
total = 0
for i in b[:a]:
    total += int(i)
print(total)