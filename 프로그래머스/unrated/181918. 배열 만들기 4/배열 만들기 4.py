def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        # for i in range(len(arr)):
        if stk == []:
            stk.append(arr[i])
            print(f"if.stk : {stk}")

            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1

        elif stk[-1] >= arr[i]:
            stk.remove(stk[-1])
            # stk.append(arr[i])
    print(stk)
    return stk


solution([1, 4, 2, 5, 3])