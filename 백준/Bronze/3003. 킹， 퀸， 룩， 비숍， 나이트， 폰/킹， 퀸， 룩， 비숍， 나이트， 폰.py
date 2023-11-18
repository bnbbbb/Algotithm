import sys
dic = {0:1, 1:1, 2:2,3:2,4:2,5:8 }
S = sys.stdin.readline().split()
a = ''
for s in range(len(S)):
    if int(S[s]) >= dic[s]:
        b = str(dic[s] - int(S[s]))
        # print('if', b)
    # elif S[s] < dic[s]:
    else:
        b = str(dic[s] - int(S[s]))
    a += b+ ' '
print(a)