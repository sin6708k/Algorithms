# 플로이드
# Gold IV
# https://www.acmicpc.net/problem/11404
from sys import stdin
from copy import deepcopy
from itertools import product, islice


def read_input():
    N = int(stdin.readline())
    M = int(stdin.readline())
    graph = [[10 ** 9 if v != u else 0
              for u in range(N + 1)]
             for v in range(N + 1)]

    for _ in range(M):
        v, u, w = map(int, stdin.readline().split())
        graph[v][u] = min(graph[v][u], w)
    return N, M, graph


def solve(N: int, M: int, graph: list[list[int]]):
    costs = deepcopy(graph)
    for k, v, u in product(range(1, N + 1), repeat=3):
        costs[v][u] = min(costs[v][u], costs[v][k] + costs[k][u])
    return costs


def print_output(costs: list[list[int]]):
    print('\n'.join(' '.join(map(str, (w if w < 10 ** 9 else 0
                                       for w in islice(edge, 1, None))))
                    for edge in islice(costs, 1, None)))


if __name__ == '__main__':
    print_output(solve(*read_input()))
