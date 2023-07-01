def solution(s):
    a = len(s)
    return s[a//2] if a % 2 !=0 else s[a//2-1:a//2+1]