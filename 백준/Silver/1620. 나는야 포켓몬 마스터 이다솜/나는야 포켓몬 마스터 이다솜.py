import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for i in range(n):
    poket = sys.stdin.readline().strip()
    dic[poket] = i+1
    dic[str(i+1)] = poket

    
for _ in range(m):
    question = sys.stdin.readline().strip()
    print(dic[question])