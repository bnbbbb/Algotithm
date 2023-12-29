n = int(input())
work = set()
for _ in range(n):
    name, status = input().split()

    if status == 'enter':
        work.add(name)
    elif status == 'leave' and name in work:
        work.remove(name)

for person in sorted(work, reverse=True):
    print(person)