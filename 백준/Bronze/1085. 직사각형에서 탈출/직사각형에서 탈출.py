x, y, w, h = map(int, input().split())

min_horizontal = min(x, w - x)

min_vertical = min(y, h - y)

result = min(min_horizontal, min_vertical)

print(result)
