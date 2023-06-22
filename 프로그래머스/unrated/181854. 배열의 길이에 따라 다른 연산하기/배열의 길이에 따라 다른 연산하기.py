def solution(arr, n):

    return [arr[i] + n if (len(arr) % 2 == 0 and i % 2 == 1) or 
         (len(arr) % 2 == 1 and i % 2 == 0) 
         else arr[i] for i in range(len(arr))]