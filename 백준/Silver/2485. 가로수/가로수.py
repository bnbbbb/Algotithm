import sys
def is_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(sys.stdin.readline())
trees = [int(sys.stdin.readline()) for _ in range(N)]

gaps = [trees[i+1] - trees[i] for i in range(0, len(trees)-1)]
gcd = gaps[0]
for num in gaps:
    gcd = is_gcd(gcd, num)
result = int((trees[-1] - trees[0])/gcd - N + 1)
print(result)