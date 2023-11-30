a, b = map(int, input().split())
a_li = [i for i in range(1, a+1) if a % i == 0]
if len(a_li) < b:
    print(0)
else:
    print(a_li[b-1])