from collections import Counter as C
import sys
n, m = map(int, sys.stdin.readline().split())
words = []
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        words.append(word)

words = C(words)

counter_words = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
for word in counter_words:
    print(word[0])