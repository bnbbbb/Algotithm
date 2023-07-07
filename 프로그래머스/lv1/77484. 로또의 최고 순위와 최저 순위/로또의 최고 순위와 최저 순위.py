def solution(lottos, win_nums):
    answer = []
    con = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    count = 0
    for i in lottos:
        if i in win_nums:
            count +=1
    zero = lottos.count(0)
    answer.extend([con[count+zero], con[count]])
    return answer