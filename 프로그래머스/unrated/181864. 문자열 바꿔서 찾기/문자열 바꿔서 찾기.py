def solution(myString, pat):
    answer = ''.join([i.replace('A', 'B') if i == 'A' else i.replace('B','A') for i in myString ])
    return int(pat in answer)