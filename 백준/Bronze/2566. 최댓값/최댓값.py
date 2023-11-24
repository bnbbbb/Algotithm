N = [list(map(int, input().split())) for _ in range(9)]
max_value = float('-inf')
for i in range(len(N)):
    if max(N[i]) > max_value:
        arr = []
        max_value = max(N[i])
        arr.extend([i+1, N[i].index(max_value)+1])
print(max_value)
print(*arr)