a = input().lower()
s = set(a)
d = {}
for i in s:
    d[i] = a.count(i)
max_count = max(d.values())

max_letters = [k for k, v in d.items() if v == max_count]
if len(max_letters) == 1:
    print(max_letters[0].upper())
else:
    print('?')