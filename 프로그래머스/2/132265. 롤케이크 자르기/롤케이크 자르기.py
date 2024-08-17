1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    set_dic = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer