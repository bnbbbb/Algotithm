def count_money(m, count, arr):
    if m == 0:
        return count
    else:
        arr = again_arr(arr, m)
        count += m // arr[0]
        m %= arr[0]
        return count_money(m, count, arr) 

def again_arr(arr, m):
    return [i for i in arr if m>=i]

n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)], reverse=True)
count = 0

result = count_money(m, count, arr)
print(result)
