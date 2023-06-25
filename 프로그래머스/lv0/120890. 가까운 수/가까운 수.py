def solution(array, n):
    array.sort()
    a = [abs(i-n) for i in array]
    b = a.index(min(a))
    return array[b]