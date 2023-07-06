def solution(dartResult):
    scores = []
    idx = 0
    score = ''
    while idx != len(dartResult):
        if dartResult[idx].isdigit():
            score += dartResult[idx]
            idx += 1
        else:   
            if dartResult[idx] == 'S':
                scores.append(int(score) ** 1)
            elif dartResult[idx] == 'D':
                scores.append(int(score) ** 2)
            elif dartResult[idx] == 'T':
                scores.append(int(score) ** 3)
            elif dartResult[idx] == '*': 
                if idx < 4:
                    scores[0] *= 2
                else:
                    scores[-1] *=2
                    scores[-2] *=2
            elif dartResult[idx] == '#':
                scores[-1] *= -1
            idx += 1
            score = ''
            
            
            
    return sum(scores)