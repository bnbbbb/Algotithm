import ast

def solution(s):
    answer = []
    result =  ast.literal_eval(s.replace("{", "[").replace("}", "]"))
    result = sorted(result, key= lambda x: len(x))
    
    for i in result:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer