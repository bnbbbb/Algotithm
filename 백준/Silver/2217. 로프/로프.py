N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort(reverse=True)

max_weight = 0

for i in range(N):
    current_weight = ropes[i] * (i + 1)
    max_weight = max(max_weight, current_weight)

print(max_weight)
