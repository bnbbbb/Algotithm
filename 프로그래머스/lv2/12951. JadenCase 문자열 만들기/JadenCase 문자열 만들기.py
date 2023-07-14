def solution(s):
    answer = [word.capitalize() for word in s.lower().split(' ')]
    
    return ' '.join(answer)