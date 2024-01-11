def recursion(s, l, r, count):  
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count+1)
    

def palindrome(s):
    count = 1
    return recursion(s, 0, len(s)-1, count)
    

n = int(input())

for _ in range(n):
    s = input()
    print(*palindrome(s))