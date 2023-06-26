def solution(lines):
    answer = []
    count = 0

    for i in lines:
        answer.append(list(range(i[0], i[1]+1)))
    a = set(answer[0]) & set(answer[1])
    b = set(answer[1]) & set(answer[2])
    c = set(answer[0]) & set(answer[2])
    if a & b:
        a = a | b |c
        return len(a)-1
    elif b & c:
        a = a | b |c
        return len(a)-1
    elif a & c:
        a = a | b |c
        return len(a)-1
    x = [len(lst)-1 for lst in (a, b, c) if len(lst) > 1]
    # x = list(x)
    print(x)
    count = sum(x)
    print(count)
    return count