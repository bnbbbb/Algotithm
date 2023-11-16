import sys
S = sys.stdin.readline().rstrip()
alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
a = ''
for al in alphabet:
    if S.find(al) != -1:
        a += str(S.find(al)) + ' '
    else:
        a += '-1 '
print(a)