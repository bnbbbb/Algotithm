x = {0: "SUN", 1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT"}

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a, b = map(int, input().split())

b = (sum(day[: a - 1]) + b) % 7
print(x.get(b))