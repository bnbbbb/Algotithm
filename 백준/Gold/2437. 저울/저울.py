n = int(input())
weights = list(map(int, input().split()))
weights.sort()
measurable_weight = 1

for weight in weights:
    if weight <= measurable_weight:
        measurable_weight += weight
    else:
        break

print(measurable_weight)