a = int(input())
b = list(map(int, input().split()))
b.sort(reverse=True)
c = max(b)

for i in range(0, a):
    b.insert(i, round(b[i] / c * 100,2))
    b.pop(i+1)


print(sum(b)/a)
# i가 0일 때 에러나서 remove대신 pop을 사용