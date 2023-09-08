def solution(arr):
    def compress(x, y, n):
        if n == 1:
            return [0, 1] if arr[y][x] == 1 else [1, 0]
        
        n //= 2
        results = [compress(x, y, n), compress(x+n, y, n), compress(x, y+n, n), compress(x+n, y+n, n)]
        
        total = [0,0]
        for result in results:
            total[0] += result[0]
            total[1] += result[1]
        if total[0] == 0:
            return [0, 1]
        elif total[1] == 0:
            return [1, 0]
        else:
            return total
    result = compress(0, 0, len(arr))
    return result