n = int(input())
result = []
arr = [300, 60, 10]
for i in range(3):
    if n % 10 != 0:
        result.append(-1)
        break
    else:
        result.append(n // arr[i])
        n %= arr[i]
print(*result)