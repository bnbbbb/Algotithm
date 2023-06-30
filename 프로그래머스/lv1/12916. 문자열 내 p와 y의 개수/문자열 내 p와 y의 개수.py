def solution(s):
    s = s.replace('P', 'p').replace('Y','y')
    
    return s.count('p') == s.count('y')