def solution(s, skip, index):
    answer = ''
    result = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        result = result.replace(i, '')
    for i in s:
        if result.find(i)+index >= len(result):
            answer += result[(result.find(i)+index) % len(result)]
        else:
            answer += result[result.find(i)+index]
    return answer