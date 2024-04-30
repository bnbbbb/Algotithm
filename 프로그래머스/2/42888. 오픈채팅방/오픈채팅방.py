def solution(record):
    answer = []
    check = {}
    for i in range(len(record)):
        record[i] = record[i].split()
        if record[i][0] != 'Leave':
            status, iden, name = record[i]
            check[iden] = name
            
    for i in range(len(record)):
        if record[i][0] == 'Enter':
            status, iden, name = record[i]
            answer.append(f'{check[iden]}님이 들어왔습니다.')
        elif record[i][0] == 'Leave':
            status, iden = record[i]
            answer.append(f'{check[iden]}님이 나갔습니다.')
    return answer