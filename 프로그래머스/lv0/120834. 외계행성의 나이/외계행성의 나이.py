def solution(age):
    answer = ''
    return ''.join([chr(int(i)+97) for i in str(age)])