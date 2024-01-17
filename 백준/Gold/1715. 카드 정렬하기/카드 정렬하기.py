import heapq

def min_card_comparisons(cards):
    heapq.heapify(cards)
    result = 0

    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)

        merge = a + b
        result += merge

        heapq.heappush(cards, merge)
    return result

N = int(input())
cards = [int(input()) for _ in range(N)]

result = min_card_comparisons(cards)
print(result)