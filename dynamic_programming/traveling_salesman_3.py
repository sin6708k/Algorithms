# 외판원 순회 3
# Gold I
# https://www.acmicpc.net/problem/16991
from sys import stdin
from typing import Iterator
from math import dist


def bit(v: int) -> int:
    return 2 ** v


def full_bit(v: int) -> int:
    return bit(v + 1) - 1


def bit_iter(bitarray: int) -> Iterator[int]:
    return iter(v for v in range(bitarray.bit_length() + 1)
                if bitarray & bit(v) != 0)


def params():
    N = int(stdin.readline())
    vertices = [tuple(map(int, stdin.readline().split()))
                for _ in range(N)]
    return N, vertices


def solution(N: int, vertices: list[tuple[int, int]]):
    VISITED_ALL = full_bit(N - 1)
    START = 0

    cost = [[10 ** 9] * N
            for _ in range(VISITED_ALL + 1)]
    cost[bit(START)][START] = 0

    for visited in range(bit(START), VISITED_ALL + 1, 2):
        for v in bit_iter(visited ^ bit(START)):
            cost[visited][v] = min((cost[visited ^ bit(v)][u] + dist(vertices[u], vertices[v])
                                    for u in bit_iter(visited ^ bit(v))),
                                   default=0)

    return min(cost[VISITED_ALL][end] + dist(vertices[end], vertices[START])
               for end in range(N)
               if end != START)


if __name__ == '__main__':
    print(solution(*params()))
