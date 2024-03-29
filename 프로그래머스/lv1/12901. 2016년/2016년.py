def solution(a, b):
    result = 0
    day = {1:'FRI',2:'SAT', 3: 'SUN', 4:'MON', 5:'TUE', 6:'WED', 7:'THU'}
    mon = {1:31,2:29, 3: 31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if a == 1:
        result += b
    else:
        for i in range(1, a):
            result += mon[i]
        result += b
    if result % 7 == 0:
        result = 7
    else:
        result %= 7
    return day[result]