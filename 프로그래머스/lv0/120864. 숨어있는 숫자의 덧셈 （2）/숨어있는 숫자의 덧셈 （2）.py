import re
def solution(my_string):
    a = re.findall(r'\d+', my_string)
    answer = sum([int(i) for i in a])
    return answer