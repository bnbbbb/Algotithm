a = input().rstrip()
n = set(map(int, input().split()))
a1 = input().rstrip()
n1 = list(map(int, input().split()))

for i in n1:
    if i in n:
        print('1', end=' ')
    else:
        print('0', end=' ')