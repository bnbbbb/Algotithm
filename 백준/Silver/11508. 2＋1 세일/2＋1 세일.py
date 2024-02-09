n = int(input())
milks = [int(input()) for _ in range(n)]
milks.sort(reverse=True)

discount = 0
for i in range(2, n, 3):
    discount += milks[i]

total = sum(milks)
print(total - discount)