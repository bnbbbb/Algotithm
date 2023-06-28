def solution(rsp):
    return ''.join(['2' if i == '5' else '5' if i=='0'  else '0' for i in rsp])
