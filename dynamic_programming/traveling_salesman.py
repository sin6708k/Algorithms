# 외판원 순회
# Gold I
# https://www.acmicpc.net/problem/2098
from sys import stdin
from math import log2, floor
from typing import Iterator


def bit(v: int) -> int:
    return 2 ** v


def all_bits(v: int) -> int:
    return bit(v + 1) - 1


def top(bits: int) -> int:
    return floor(log2(bits)) if bits != 0 else -1


def bit_iter(bits: int) -> Iterator[int]:
    return iter(v for v in range(top(bits) + 1)
                if bits & bit(v) != 0)


def params():
    N = int(stdin.readline())
    graph = [[w if w != 0 else
              10 ** 9 if v != u else 0
              for u, w in enumerate(map(int, stdin.readline().split()))]
             for v in range(N)]
    return N, graph


def solution(N: int, graph: list[list[int]]):
    VISITED_ALL = all_bits(N - 1)
    START = 0

    cost = [[10 ** 9] * N
            for _ in range(VISITED_ALL + 1)]
    cost[bit(START)][START] = 0

    for visited in range(bit(START), VISITED_ALL + 1, 2):
        for v in bit_iter(visited ^ bit(START)):
            cost[visited][v] = min((cost[visited ^ bit(v)][u] + graph[u][v]
                                    for u in bit_iter(visited ^ bit(v))),
                                   default=0)

    return min(cost[VISITED_ALL][end] + graph[end][START]
               for end in range(N)
               if end != START)


if __name__ == '__main__':
    print(solution(*params()))
