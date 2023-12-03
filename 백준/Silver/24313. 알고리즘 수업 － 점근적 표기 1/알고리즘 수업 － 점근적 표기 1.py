a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

result = any(a1 * i + a0 > c * i for i in range(n0, 101))
print(0 if result else 1)