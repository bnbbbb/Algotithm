import sys

def solution():
    n, k = map(int, sys.stdin.readline().split())
    table = list(sys.stdin.readline().rstrip())
    result = 0
    
    for i in range(n):
        if table[i] == 'P':
            for j in range(i - k, i + k + 1):
                if 0 <= j < n and table[j] == 'H':
                    result += 1
                    table[j] = 'E'  # 햄버거를 먹은 사람 표시
                    break
    print(result)

solution()