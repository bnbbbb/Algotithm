def solution(s):
    s = s.split(' ')
    s = sorted(s, key = lambda x: int(x))
    
    return f'{s[0]} {s[-1]}'  
