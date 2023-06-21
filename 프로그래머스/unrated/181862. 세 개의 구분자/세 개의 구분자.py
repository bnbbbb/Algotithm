import re
def solution(myStr):
    answer = [i for i in re.split('[abc]', myStr) if i != '']
    if answer == []:
        answer.append('EMPTY')
        
    return answer