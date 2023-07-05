def solution(N, stages):
    answer = []
    dic = {}
    a = len(stages)
    for i in range(1, N+1):
        if a == 0:
            dic[i] = 0
        else:
            dic[i] = (stages.count(i)/a)
            a -= stages.count(i)
    answer = sorted(dic, key = dic.get, reverse=True)
    return answer