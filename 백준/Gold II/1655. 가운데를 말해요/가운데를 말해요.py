import heapq, sys

def find_median(arr):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙
    result = []

    for x in arr:
        # 최대 힙과 최소 힙에 값을 추가
        if not max_heap or x <= -max_heap[0]:
            heapq.heappush(max_heap, -x)
        else:
            heapq.heappush(min_heap, x)

        # 최대 힙과 최소 힙의 크기를 맞춤
        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        while len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # 중간값 계산
        if len(max_heap) == len(min_heap):
            median = min(-max_heap[0], min_heap[0])
        else:
            median = -max_heap[0]

        result.append(median)

    return result

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for _ in range(N)]

    result = find_median(numbers)

    for median in result:
        print(median)