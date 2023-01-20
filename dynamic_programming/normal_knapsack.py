# 평범한 배낭
# https://www.acmicpc.net/problem/12865
from sys import stdin


if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    items = [tuple(map(int, stdin.readline().split()))
             for _ in range(N)]
    value_memo = [[0] * (N + 1)
                  for _ in range(K + 1)]

    items.sort(key=lambda x: (x[0], x[1]))

    for w in range(1, K + 1):
        for i, (weight, value) in enumerate(items, 1):
            value_memo[w][i] = max(value_memo[w - weight][i - 1] + value,
                                   value_memo[w][i - 1]) if weight <= w else value_memo[w][i - 1]

    print(value_memo[K][N])
