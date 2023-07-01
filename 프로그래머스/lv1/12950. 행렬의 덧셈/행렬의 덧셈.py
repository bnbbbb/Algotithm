def solution(arr1, arr2):
    answer = []
    rows = len(arr1)
    cols = len(arr1[0])
    for i in range(rows):
        a = []
        for j in range(cols):
            a.append(arr1[i][j] + arr2[i][j])
        answer.append(a)
    return answer