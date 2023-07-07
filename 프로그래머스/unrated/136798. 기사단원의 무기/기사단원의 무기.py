def solution(number, limit, power):
    answer = []
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                if j * j == i:
                    count +=1
                else:
                    count += 2
        answer.append(count)
    for idx, value in enumerate(answer):
        if value > limit:
            answer[idx] = power
    return sum(answer)