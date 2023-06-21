def solution(arr, flag):
    answer = list(zip(arr, flag))
    result = [i for i, j in answer  for x in range(i*2)]
    result = []
    for i, j in answer:
        if j == True:
            for x in range(i*2):
                result.append(i)
        else:
            for x in range(i):
                result.pop()
    return result
