# 최단경로
# https://www.acmicpc.net/problem/1753
from sys import stdin
from heapq import heappush, heappop
from itertools import islice


if __name__ == '__main__':
    V, E = map(int, stdin.readline().split())
    K = int(stdin.readline())
    W = 10 * 20000 + 1
    graph = [[] for _ in range(V + 1)]  # v = 0 is unused
    dist_memo = [W] * (V + 1)
    to_visit = []

    for _ in range(E):
        v, u, w = map(int, stdin.readline().split())
        graph[v].append((u, w))

    dist_memo[K] = 0
    heappush(to_visit, (0, K))

    while to_visit:
        dist, v = heappop(to_visit)
        if dist_memo[v] < dist:
            continue

        for u, w in graph[v]:
            next_dist = dist + w
            if next_dist < dist_memo[u]:
                dist_memo[u] = next_dist
                heappush(to_visit, (next_dist, u))

    print('\n'.join((str(dist) if dist < W else 'INF'
                     for dist in islice(dist_memo, 1, None))))
