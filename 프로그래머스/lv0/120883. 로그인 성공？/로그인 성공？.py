def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw[0] in i:
            if id_pw[1] == i[1]:
                answer = 'login'
                return answer
            else:
                answer = 'wrong pw'
                return answer
        else:
            answer = 'fail'
    return answer