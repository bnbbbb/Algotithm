def solution(s):
    answer = ''
    return ''.join(sorted([i for i in s if s.count(i) == 1]))