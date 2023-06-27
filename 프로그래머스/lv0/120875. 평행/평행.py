def solution(dots):
    answer = []
    result = []
    count = 0
    for i in range(1, len(dots)):
        select = [dots[0],dots[i]]
        answer.append([dots[0], dots[i]])
        answer.append([i for i in dots if i not in select])
    print(answer)
    for i in answer:
        result.append((i[0][1]-i[1][1])/(i[0][0]-i[1][0]))
    print(result)
    for i in range(0, len(result), 2):
        if result[i] == result[i+1]:
            count+=1
    return int(count >= 1)
