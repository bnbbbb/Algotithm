
def card_mix(n, m, cards):
    for _ in range(m):
        cards.sort()
        result = cards[0] + cards[1]
        cards[0] = result
        cards[1] = result
    return sum(cards)

n, m = map(int, input().split())
cards = list(map(int, input().split()))
print(card_mix(n, m, cards))