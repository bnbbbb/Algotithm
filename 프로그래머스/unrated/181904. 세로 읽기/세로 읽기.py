def solution(my_string, m, c):
    answer = []
    result = ""
    for i in range(len(my_string) // m):
        answer.append(my_string[i * m : m * (i + 1)])
    for i in answer:
        result += i[c - 1]
    return result