def campping(l, p, v):
    a, b = divmod(v, p)
    if b > l:
        return a * l + l
    else:
        return a * l + b
idx =1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v==0:
        break
    print(f'Case {idx}: {campping(l, p, v)}')
    idx += 1