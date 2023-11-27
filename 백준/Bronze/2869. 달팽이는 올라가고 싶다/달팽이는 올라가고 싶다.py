import math
a,b,v = map(int, input().split())

c = v - a
c = math.ceil(c/(a-b))
print(c+1)