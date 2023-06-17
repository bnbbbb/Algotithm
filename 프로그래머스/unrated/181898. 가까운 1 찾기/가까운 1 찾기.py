def solution(arr, idx):
    answer = idx
    arr = arr[idx:]

    if 1 in arr:
        answer += arr.index(1)
    else:
        return -1
    return answer


solution([0, 0, 0, 1, 1], 1)