N =  int(input())
for _ in range(N):
    n = int(input())    
    a = [0,0,0,0]
    while n > 0:
        if n >= 25:
            m, r = divmod(n , 25)
            a[0] = m
            n = r
        elif 25 > n >= 10:
            m, r = divmod(n, 10)
            a[1] = m
            n = r
        elif 10 > n >= 5:
            m, r = divmod(n, 5)
            a[2] = m
            n = r
        else:
            a[3] = n
            n = 0
    print(*a)