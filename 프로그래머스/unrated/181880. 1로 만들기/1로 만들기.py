def solution(arr):
    answer = 0

    for i in range(len(arr)):
        while arr[i] != 1:
            if arr[i] % 2 == 0:
                arr[i] = arr[i] / 2 
                answer += 1
            elif arr[i] % 2 == 1:
                arr[i] = (arr[i] -1) / 2
                answer += 1
    return answer