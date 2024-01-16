def count_money(money, counts, idx):
    for count in counts:
        if money >= count:
            idx += (money // count)
            money %= count
        else:
            continue
    return idx

count = [500, 100, 50, 10, 5, 1]

idx = 0
n = int(input())
result = count_money(1000-n, count, idx)
print(result)