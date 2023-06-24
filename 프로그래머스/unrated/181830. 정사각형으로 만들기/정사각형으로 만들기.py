def solution(arr):
    col = len(arr[0])
    row = len(arr)
    if row > col:
        for i in range(row): 
            arr[i].extend([0]*(row-col))
    elif col > row:
        for i in range(row, col):
            arr.append([0] * col)

    return arr