# 최단경로
# Gold IV
# https://www.acmicpc.net/problem/1753
from sys import stdin
from heapq import heappush, heappop
from itertools import islice


def read_input():
    V, E = map(int, stdin.readline().split())
    K = int(stdin.readline())
    graph = [[] for _ in range(V + 1)]  # v = 0 is unused

    for _ in range(E):
        v, u, w = map(int, stdin.readline().split())
        graph[v].append((u, w))
    return V, E, K, graph


def solve(V: int, E: int, K: int, graph: list[tuple[int, int]]):
    dists = [10 ** 9] * (V + 1)
    to_visit = []

    dists[K] = 0
    heappush(to_visit, (0, K))

    while to_visit:
        dist, v = heappop(to_visit)
        if dists[v] < dist:
            continue

        for u, w in graph[v]:
            if dist + w < dists[u]:
                dists[u] = dist + w
                heappush(to_visit, (dist + w, u))
    return dists


def print_output(dists: list[int]):
    print('\n'.join((str(dist) if dist < 10 ** 9 else 'INF'
                     for dist in islice(dists, 1, None))))


if __name__ == '__main__':
    print_output(solve(*read_input()))
