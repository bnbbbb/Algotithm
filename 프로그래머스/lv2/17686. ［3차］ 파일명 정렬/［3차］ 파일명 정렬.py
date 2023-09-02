import re
def solution(files):
    answer = []
    
    for file in files:
        matches = re.match(r'([a-zA-Z?.+\-\s]+)(\d+)', file)
        if matches:
            group1 = matches.group(1)
            group2 = matches.group(2)
            answer.append((group1, group2, file))
    answer.sort(key= lambda x: (x[0].lower(), int(x[1])))
    answer = [i[2] for i in answer]
    return answer