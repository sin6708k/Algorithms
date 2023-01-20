# 플로이드
# https://www.acmicpc.net/problem/11404
from sys import stdin


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

    for k in range(1, N + 1):
        for v in range(1, N + 1):
            for u in range(1, N + 1):
                graph[v][u] = min(graph[v][u], graph[v][k] + graph[k][u])

    print('\n'.join(' '.join(map(str, (w if w < W else 0
                                       for w in edge[1:])))
                    for edge in graph[1:]))
