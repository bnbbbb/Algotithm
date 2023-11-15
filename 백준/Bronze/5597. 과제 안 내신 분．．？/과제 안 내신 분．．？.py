a = [i+1 for i in range(30)]
for i in range(28):
    b = int(input())
    if b in a:
        a.remove(b)

print(min(a))
print(max(a))