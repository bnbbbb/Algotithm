def solution(arr):
    while bin(len(arr)).count('1') != 1:
        arr.append(0)
    return arr