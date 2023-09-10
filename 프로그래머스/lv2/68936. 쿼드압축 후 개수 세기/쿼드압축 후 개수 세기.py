def spliter(arr):
    size = len(arr)//2
    lu = [i[:size] for i in arr[:size]]
    lb = [i[:size] for i in arr[size:]]
    ru = [i[size:] for i in arr[:size]]
    rb = [i[size:] for i in arr[size:]]
    return lu, lb, ru, rb

def ziper(arr):
    size = len(arr)
    s = sum(sum(i) for i in arr)
    if s == size**2:
        return [1]
    elif s == 0:
        return [0]
    else:
        lu, lb, ru, rb = spliter(arr)
        return ziper(lu) + ziper(lb) + ziper(ru) + ziper(rb)

def solution(arr):
    zip_res = ziper(arr)

    return [len(zip_res) - sum(zip_res), sum(zip_res)]