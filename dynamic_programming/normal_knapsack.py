# 평범한 배낭
# Gold V
# https://www.acmicpc.net/problem/12865
from sys import stdin
from itertools import product


def params():
    N, K = map(int, stdin.readline().split())
    items = sorted([tuple(map(int, stdin.readline().split()))
                    for _ in range(N)])
    return N, K, items


def solution(N: int, K: int, items: list[int]):
    value = [[0] * (K + 1)
             for _ in range(N + 1)]

    for (i, (w_i, v_i)), w in product(enumerate(items, 1), range(1, K + 1)):
        if w_i <= w:
            value[i][w] = max(value[i - 1][w],
                              value[i - 1][w - w_i] + v_i)
        else:
            value[i][w] = value[i - 1][w]

    return value[-1][-1]


if __name__ == '__main__':
    print(solution(*params()))
