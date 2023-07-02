import string

tmp = string.digits+string.ascii_lowercase

def convert(num) :
    q, r = divmod(num, 3)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q) + tmp[r]
def solution(n):
    answer = ''
    answer += convert(n)
    answer = answer[::-1]
    return int(answer,3)