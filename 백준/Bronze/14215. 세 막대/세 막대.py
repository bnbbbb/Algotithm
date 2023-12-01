a = list(map(int, input().split()))
a.sort(reverse=True)

other_sides_sum = a[1] + a[2]

if a[0] < other_sides_sum:
    print(sum(a))
else:
    a[0] = a[1] + a[2] -1
    print(sum(a))
