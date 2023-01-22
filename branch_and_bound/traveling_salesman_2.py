# 외판원 순회 2
# https://www.acmicpc.net/problem/10971
from sys import stdin
from collections import deque


def search(v: int, cost: int):
    global N
    global path
    global min_cost

    if cost >= min_cost:
        return

    if len(path) + 1 == N:
        u = path[0]
        min_cost = min(min_cost, cost + graph[v][u])
        return

    path.append(v)
    for u in range(N):
        if u not in path:
            search(u, cost + graph[v][u])
    path.pop()


if __name__ == '__main__':
    N = int(stdin.readline())
    W = 1000000 * N + 1
    graph = [[w if w != 0 else
              W if v != u else 0
              for u, w in enumerate(map(int, stdin.readline().split()))]
             for v in range(N)]
    path = deque()
    min_cost = W

    search(0, 0)
    print(min_cost)
