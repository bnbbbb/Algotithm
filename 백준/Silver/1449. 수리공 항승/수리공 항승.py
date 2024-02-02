def minimum(n, l, leaks):
    leaks.sort()
    
    taps = 0
    current = 0
    
    for leak in leaks:
        if leak-0.5 >= current:
            current = leak + (l - 0.5)
            taps += 1
    return taps

n, l = map(int, input().split())

leaks = list(map(int, input().split()))
print(minimum(n, l, leaks))