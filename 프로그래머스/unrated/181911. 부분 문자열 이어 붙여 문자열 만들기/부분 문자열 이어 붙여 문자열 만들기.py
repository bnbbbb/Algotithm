def solution(my_strings, parts):
    result = ""
    answer = list(zip(my_strings, parts))

    for i, j in answer:
        result += i[j[0] : j[1] + 1]

    return result