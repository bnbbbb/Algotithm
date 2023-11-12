import re

def solution(info, query):
    answer = []
    info_dict = {}
    
    for i in info:
        data = i.split()
        conditions = data[:-1]
        score = int(data[-1])
        for condition in range(16):
            key = ''
            for j in range(4):
                if condition & (1 << j):
                    key += conditions[j]
                else:
                    key += '-'
            if key in info_dict:
                info_dict[key].append(score)
            else:
                info_dict[key] = [score]
    
    for key in info_dict:
        info_dict[key].sort()

    for q in query:
        q = re.sub(' and | ', ' ', q).split()
        query_key = ''.join(q[:-1])
        min_score = int(q[-1])

        if query_key in info_dict:
            scores = info_dict[query_key]
            left, right = 0, len(scores)
            
            while left < right:
                mid = (left + right) // 2
                if scores[mid] < min_score:
                    left = mid + 1
                else:
                    right = mid
            
            answer.append(len(scores) - left)
        else:
            answer.append(0)
    return answer
