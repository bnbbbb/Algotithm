import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub(r'[^\w\d_.-]', '', new_id)
    new_id = re.sub(r"\.{2,}", ".", new_id)
    if new_id == '.':
        new_id = ''
    else:
        if new_id[0]=='.':
            new_id = new_id[1:]
        if new_id[-1]=='.': 
            new_id = new_id[:-1]
    if new_id == '':
        new_id+='a'
    if len(new_id) >= 16:
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id