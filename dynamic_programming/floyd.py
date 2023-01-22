# 플로이드
# https://www.acmicpc.net/problem/11404
from sys import stdin
from itertools import product, islice


if __name__ == '__main__':
    N = int(stdin.readline())
    M = int(stdin.readline())
    W = 100000 * N
    graph = [[W if v != u else 0
              for u in range(N + 1)]
             for v in range(N + 1)]

    for _ in range(M):
        v, u, w = map(int, stdin.readline().split())
        graph[v][u] = min(graph[v][u], w)

    for k, v, u in product(range(1, N + 1), repeat=3):
        graph[v][u] = min(graph[v][u], graph[v][k] + graph[k][u])

    print('\n'.join(' '.join(map(str,
                                 (w if w < W else 0
                                  for w in islice(edge, 1, None))))
                    for edge in islice(graph, 1, None)))
