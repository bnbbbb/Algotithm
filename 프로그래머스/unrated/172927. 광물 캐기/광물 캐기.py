def solution(picks, minerals):
    answer = 0
    di = {'diamond': 1, 'iron': 1, 'stone': 1}
    ir = {'diamond': 5, 'iron': 1, 'stone': 1}
    st = {'diamond': 25, 'iron': 5, 'stone': 1}
    dic = {'diamond': picks[0], 'iron': picks[1], 'stone': picks[2]}
    sum_pick = sum(picks)
    count = []
    
    for i in range(0, min(len(minerals), sum_pick*5), 5):
        dia = minerals[i:i+5].count('diamond')
        iron = minerals[i:i+5].count('iron')
        stone = minerals[i:i+5].count('stone')
        count.append((i, dia, iron, stone))
    count.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)
    
    for i in count:
        if dic['diamond'] > 0:
            answer += i[1] + i[2] + i[3]
            dic['diamond'] -=1
        elif dic['iron'] > 0:
            answer += i[1] * 5 + i[2] + i[3]
            dic['iron'] -=1
        else:
            answer += i[1] * 25 + i[2] * 5 + i[3]
            dic['stone'] -=1
    return answer