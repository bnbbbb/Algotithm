def distance(n, k, sersor):
    sersor.sort()  
    gaps = []  

    for i in range(1, n):
        gaps.append(sersor[i] - sersor[i - 1])

    gaps.sort(reverse=True)
    for _ in range(k - 1):
        if gaps:
            gaps.pop(0)
            
    return sum(gaps)

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

result = distance(n, k, sensor)
print(result)
