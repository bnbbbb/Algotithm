total = int(input()) 
leng = int(input())
total_won = 0
sum = 0
for _ in range(leng):
    x, y = map(int, input().split())
    sum += x * y
if total == sum:
    print('Yes')
else:
    print('No')