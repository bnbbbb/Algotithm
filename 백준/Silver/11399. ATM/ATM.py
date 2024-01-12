n = int(input())

arr = list(map(int, input().split()))
arr.sort()

s = 0
a = 0
for i in range(n):
    s += arr[i]
    a += s
print(a)