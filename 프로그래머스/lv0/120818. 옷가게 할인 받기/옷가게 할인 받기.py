import math
def solution(price):
    return math.floor(price * 0.8 if price >= 500000 else (price * 0.9 if price >= 300000 else (0.95 * price if price >= 100000 else price)))