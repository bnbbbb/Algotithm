def solution(arr):
    answer = []
    return arr if arr.remove(min(arr)) != [] else  [-1]