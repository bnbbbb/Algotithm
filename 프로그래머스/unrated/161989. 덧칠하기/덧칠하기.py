def solution(n, m, section):
    count = 0
    flag = 0

    for start in section:
        end = min(start + m - 1, n)

        if start > flag:
            count += 1
            flag = end

    return count
