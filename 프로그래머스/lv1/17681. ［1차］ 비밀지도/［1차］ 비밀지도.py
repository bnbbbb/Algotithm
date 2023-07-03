def solution(n, arr1, arr2):
    answer = []
    a = []
    b = []
    for i in arr1:
        a.append(bin(i)[2:].zfill(n))
    for i in arr2:
        b.append(bin(i)[2:].zfill(n))
        
    for i, j in zip(a, b):
        row = ''
        for x, y in zip(i, j):
            if x == '1' or y == '1':
                row += '#'
            else:
                row += ' '
        answer.append(row)
    return answer