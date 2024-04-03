n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        # 오른쪽 위에서 내려오는 경우
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]
        # 그 외의 경우
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
print(max(triangle[n - 1]))