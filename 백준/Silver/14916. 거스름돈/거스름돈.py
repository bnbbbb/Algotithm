def min_coins(n):
    count_5 = n // 5
    remaining = n % 5
    
    while count_5 >= 0:
        if remaining % 2 == 0:
            count_2 = remaining // 2
            return count_5 + count_2
        else:
            count_5 -= 1
            remaining += 5

    return -1

n = int(input())

result = min_coins(n)
print(result)