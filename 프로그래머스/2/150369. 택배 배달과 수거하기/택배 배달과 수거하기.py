def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    to_deli = 0
    to_pick = 0

    for i in range(n):
        to_deli += deliveries[i]
        to_pick += pickups[i]

        while to_deli > 0 or to_pick > 0:
            to_deli -= cap
            to_pick -= cap
            answer += (n - i) * 2

    return answer