def solution(arr, k):
    answer = []
    return [i * k if k % 2 == 1 else i + k for i in arr]