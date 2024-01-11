def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr)+1)//2
    low_arr = merge(arr[:mid])
    high_arr = merge(arr[mid:])
    sorted_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] <= high_arr[h]:
            sorted_arr.append(low_arr[l])
            answer.append(low_arr[l])
            l += 1
        else:
            sorted_arr.append(high_arr[h])
            answer.append(high_arr[h])
            h += 1
    while l < len(low_arr):
        sorted_arr.append(low_arr[l])
        answer.append(low_arr[l])
        l += 1
    
    while h < len(high_arr):
        sorted_arr.append(high_arr[h])
        answer.append(high_arr[h])
        h +=1
    
    return sorted_arr

answer = []
n, m = map(int, input().split())
arr = list(map(int, input().split()))
merge(arr)
print(answer[m-1] if len(answer) >= m else -1)