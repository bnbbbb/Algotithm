def change_word(s, t):
    while len(t) > len(s):
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] =='B':
            t = t[:-1][::-1]
    return 1 if s == t else 0

s = input().strip()
t = input().strip()
print(change_word(s, t))