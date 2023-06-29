def solution(array):
    result = []
    answer = [array.count(i) for i in array]
    a = dict(zip(array, answer))
    for key, value in a.items():
        if value == max(answer):
            result.append(key)
    return -1 if len(result) > 1 else result[0]