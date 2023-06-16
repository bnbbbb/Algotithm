def solution(string, queries):
    string = list(string)
    for i in queries:
        string[i[0] : i[1] + 1] = reversed(string[i[0] : i[1] + 1])
    string = "".join(string)
    return string