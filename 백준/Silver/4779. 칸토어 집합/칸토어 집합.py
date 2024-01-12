def cantor_set(n):
    if n == 0:
        return "-"
    
    base = " " * 3 ** (n - 1)
    prev_result = cantor_set(n - 1)
    return prev_result + base + prev_result
while True:
    try:
        N = int(input())
        result = cantor_set(N)
        print(result)
    except EOFError:
        break