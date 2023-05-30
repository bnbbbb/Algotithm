a = int(input())
b = []
for i in range((a//5)+1):
    for j in range((a//3)+1):
        if 5*i + 3*j == a:
            b.append(i + j)
if b == []:
    b.append(-1)
print(min(b))