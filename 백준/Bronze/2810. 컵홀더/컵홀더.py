def cupholders(n, seats):
    count = 0
    i = 0

    while i < n:
        if seats[i] == 'S':
            count += 1
            i += 1
        elif seats[i] == 'L':
            count += 1
            i += 2 

    return min(count + 1, n)

n = int(input())
seats = input()

result = cupholders(n, seats)
print(result)