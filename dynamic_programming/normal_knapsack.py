# 평범한 배낭
# https://www.acmicpc.net/problem/12865
from sys import stdin
from itertools import product


if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    items = sorted([tuple(map(int, stdin.readline().split()))
                    for _ in range(N)])
    value_memo = [[0] * (N + 1)
                  for _ in range(K + 1)]

    for w, (i, (weight, value)) in product(range(1, K + 1), enumerate(items, 1)):
        value_memo[w][i] = max(value_memo[w - weight][i - 1] + value,
                               value_memo[w][i - 1]) if weight <= w else value_memo[w][i - 1]

    print(value_memo[K][N])
