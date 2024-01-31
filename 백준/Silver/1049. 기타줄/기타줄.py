
n, m = map(int, input().split())

package_prices = []
single_prices = []

for _ in range(m):
    package, single = map(int, input().split())
    package_prices.append(package)
    single_prices.append(single)

min_package = min(package_prices)
min_single = min(single_prices)
result = 0

while n > 0:
    if n >= 6 and min_package <= min_single * 6:
        result += min_package
        n -= 6
    elif min_single * min(6, n) <= min_package:
        result += min_single * min(6, n)
        n -= min(6, n)
    else:
        result += min_package
        n -= 6

print(result)