def solution(todo_list, finished):
    answer = list(zip(todo_list, finished))
    result = []
    for i in answer:
        if i[1] == False:
            result.append(i[0])
    return result