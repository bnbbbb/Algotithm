def solution(score):
    answer = [sum(i) for i in score]
    print(answer)
    n = len(answer)
    rank = [1]*n
    for i in range(n):
        for j in range(n):
            if i != j:
                if answer[i] > answer[j]:
                    rank[j] += 1

    return rank