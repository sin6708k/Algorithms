# 외판원 순회 2
# https://www.acmicpc.net/problem/10971
from sys import stdin


def search(path: list[int], cost: int):
    global N
    global min_cost

    if cost >= min_cost:
        return

    n = len(path)
    v = path[-1]

    if n == N:
        u = path[0]
        min_cost = min(min_cost, cost + graph[v][u])
        return

    for u in range(N):
        if u not in path:
            search(path + [u], cost + graph[v][u])


if __name__ == '__main__':
    N = int(stdin.readline())
    W = 1000000 * N + 1
    graph = [[w if w != 0 else
              W if v != u else 0
              for u, w in enumerate(map(int, stdin.readline().split()))]
             for v in range(N)]
    min_cost = W

    search([0], 0)
    print(min_cost)
