# 외판원 순회
# https://www.acmicpc.net/problem/2098
from sys import stdin
from typing import Iterator


def bit(v: int) -> int:
    return 2 ** v


def all_bits(v: int) -> int:
    return bit(v + 1) - 1


def bit_iter(bits: int) -> Iterator[int]:
    return iter(v for v in range(N)
                if bits & bit(v) != 0)


if __name__ == '__main__':
    N = int(stdin.readline())
    W = 1000000 * N + 1
    VISITED_ALL = all_bits(N - 1)
    START = 0

    graph = [[w if w != 0 else
              W if v != u else 0
              for u, w in enumerate(map(int, stdin.readline().split()))]
             for v in range(N)]
    cost_memo = [[W] * N
                 for i in range(VISITED_ALL + 1)]
    cost_memo[bit(START)][START] = 0

    for visited in range(bit(START), VISITED_ALL + 1, 2):
        for v in bit_iter(visited ^ bit(START)):
            cost_memo[visited][v] = min((cost_memo[visited ^ bit(v)][u] + graph[u][v]
                                         for u in bit_iter(visited ^ bit(v))),
                                        default=0)

    print(min(cost_memo[VISITED_ALL][end] + graph[end][START]
              for end in range(N)
              if end != START))
