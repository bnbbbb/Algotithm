def solution(id_list, report, k):
    answer = []
    report = set(report)
    re = [i.split(' ') for i in report]
    id_dict = {i:0 for i in id_list}
    
    result = [i[1] for i in re]
    
    an = [i for i in id_list if result.count(i) >= k]
    
    re = [i for i in re if i[1] in an]
    
    for i in re:
        id_dict[i[0]] += 1
        
    for key, value in id_dict.items():
        answer.append(value)
    return answer