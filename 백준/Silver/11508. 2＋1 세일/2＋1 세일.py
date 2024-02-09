n = int(input())
milks = [int(input()) for _ in range(n)]
milks.sort(reverse=True)

discount = sum(milks[2::3])

total = sum(milks)
print(total - discount)