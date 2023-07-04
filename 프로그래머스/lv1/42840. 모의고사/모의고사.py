def solution(answers):
    answer = []
    result = [0,0,0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            result[0] += 1
        if answers[i] == b[i%8]:
            result[1] += 1 
        if answers[i] == c[i%10]:
            result[2] += 1
    
    for i in range(len(result)):
        if max(result) == result[i]:
            answer.append(i+1)
    print(answer)
    return answer