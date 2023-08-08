def solution(arr1, arr2):
    answer = []
    i = 0
    b = 0
    
    while i != len(arr1):
        a = []
        for j in range(len(arr2[0])):
            b = 0
            for k in range(len(arr1[0])):
                b += arr1[i][k] * arr2[k][j]
            a.append(b)
        answer.append(a)
        i += 1
    return answer