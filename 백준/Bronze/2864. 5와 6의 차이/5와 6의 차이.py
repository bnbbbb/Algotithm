n, m = input().split()

minimum = int(n.replace('6', '5')) + int(m.replace('6', '5'))
maximum = int(n.replace('5', '6')) + int(m.replace('5', '6'))
print(minimum, maximum)