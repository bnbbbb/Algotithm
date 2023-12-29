n, m = map(int, input().split())
set_a = set(input() for _ in range(n))

count = 0
for _ in range(m):
    string = input()
    if string in set_a:
        count += 1

print(count)