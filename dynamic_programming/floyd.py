# 플로이드
# Gold IV
# https://www.acmicpc.net/problem/11404
from sys import stdin
from copy import deepcopy
from itertools import product, islice


def params():
    N = int(stdin.readline())
    M = int(stdin.readline())

    graph = [[10 ** 9 if v != u else 0
              for u in range(N + 1)]
             for v in range(N + 1)]
    for _ in range(M):
        v, u, w = map(int, stdin.readline().split())
        graph[v][u] = min(graph[v][u], w)

    return N, M, graph


def solution(N: int, M: int, graph: list[list[int]]):
    cost = deepcopy(graph)
    for k, v, u in product(range(1, N + 1), repeat=3):
        cost[v][u] = min(cost[v][u], cost[v][k] + cost[k][u])

    return '\n'.join(' '.join(map(str, (w if w < 10 ** 9 else 0
                                        for w in islice(edge, 1, None))))
                     for edge in islice(cost, 1, None))


if __name__ == '__main__':
    print(solution(*params()))
