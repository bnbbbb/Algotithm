def solution(spell, dic):
    answer = []
    count = 0
    for i in dic:
        for j in spell:
            if j in i:
                count += 1
        answer.append(count)
        count = 0
    if len(spell) in answer:
        return 1
    return 2