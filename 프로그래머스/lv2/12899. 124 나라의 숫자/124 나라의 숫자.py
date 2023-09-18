import math
def solution(n):
    answer = ''
    dic = {1:'1', 2:'2', 0:'4'}
    while n != 0:
        div = math.ceil(n / 3)-1
        mod = n % 3
        n = div
        answer += dic[mod]
    return answer[::-1]