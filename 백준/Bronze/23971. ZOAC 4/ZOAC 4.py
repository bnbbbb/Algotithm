import math
h, w, n, m = map(int, input().split())
col = math.ceil(h / (n+1))
row = math.ceil(w / (m+1))
print(col * row)