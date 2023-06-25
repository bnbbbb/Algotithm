def solution(numbers):
    num = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    # print(num)
    for i, j in num.items():
        if i in numbers:
            numbers = numbers.replace(i, str(j))
    return int(numbers)