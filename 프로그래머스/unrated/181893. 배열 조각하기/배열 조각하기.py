def solution(arr, query):
    
    for i in range(len(query)):
        if i % 2 == 0:
            if arr.index(arr[-1]) == query[i]:
                arr = arr
            else:
                arr = arr[:query[i]+1]
        else:
            if arr.index(arr[0]) == query[i]:
                arr = arr
            else:
                arr = arr[query[i]:]
    return arr
