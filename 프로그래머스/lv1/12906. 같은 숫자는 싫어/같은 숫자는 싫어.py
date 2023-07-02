def solution(arr):
    # 함수를 완성하세요
    answer = []
    for i in arr:
        if answer[-1:] == [i]:
            continue
        answer.append(i)
    return answer