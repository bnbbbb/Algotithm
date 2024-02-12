for _ in range(int(input())):
    n = int(input())
    trees = sorted(list(map(int, input().split())))
    result = 0
    for i in range(2,n):
        result = max(result, abs(trees[i]-trees[i-2]))
    print(result)