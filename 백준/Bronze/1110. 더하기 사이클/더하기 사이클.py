a = input()
count = 0
if len(a) == 1:
    a += '0'
c = a
b = str(int(c[0])+int(c[1])) # 8
while(True):
    if len(b) == 1:
        b = '0'+ b
    c1 = c[1] + b[1]
    c = str(int(c[1]) + int(b[1])) # 14
    count +=1
    if len(c) == 1:
        c = '0'+ c
    b1 = b[1]+c[1]
    b = str(int(b[1]) + int(c[1])) # 12
    count +=1
    if a == c1:
        count -=1
        break
    elif a == b1:
        break
print(count)