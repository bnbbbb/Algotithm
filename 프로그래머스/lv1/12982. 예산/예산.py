def solution(d, budget):
    answer = 0
    count = 0
    while answer < budget:
        answer += min(d)
        count += 1
        d.remove(min(d))
        if d == []:
            break
    if answer > budget:
        count -= 1
    else:
        return count
    return count