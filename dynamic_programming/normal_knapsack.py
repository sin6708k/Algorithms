# 평범한 배낭
# https://www.acmicpc.net/problem/12865
from sys import stdin
from itertools import product


if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    items = sorted([tuple(map(int, stdin.readline().split()))
                    for _ in range(N)])
    value_memo = [[0] * (K + 1)
                  for _ in range(N + 1)]

    for (i, (weight, value)), w in product(enumerate(items, 1), range(1, K + 1)):
        if weight <= w:
            value_memo[i][w] = max(value_memo[i - 1][w],
                                   value_memo[i - 1][w - weight] + value)
        else:
            value_memo[i][w] = value_memo[i - 1][w]

    print(value_memo[N][K])
