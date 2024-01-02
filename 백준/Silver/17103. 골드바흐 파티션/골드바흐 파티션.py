import sys

def prime_list(n):
    arr = [True]*n
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i*i, n, i):
                arr[j] = False
    return arr

def execute():
    T = int(sys.stdin.readline())
    arr = prime_list(1000001)
    for _ in range(T):
        N = int(sys.stdin.readline())
        cnt = 0
        for n1 in range(2, N//2+1):
            if arr[n1] and arr[N-n1]:
                cnt += 1
        print(cnt)

execute()