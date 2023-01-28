# 외판원 순회 2
# Silver II
# https://www.acmicpc.net/problem/10971
from sys import stdin


def params():
    N = int(stdin.readline())
    graph = [[w if w != 0 else
              10 ** 9 if v != u else 0
              for u, w in enumerate(map(int, stdin.readline().split()))]
             for v in range(N)]
    return N, graph


def solution(N: int, graph: list[list[int]]):
    path = []
    min_cost = 10 ** 9

    def search(v: int, cost: int):
        nonlocal min_cost
        if cost >= min_cost:
            return
        if len(path) == N - 1:
            u = path[0]
            min_cost = min(min_cost, cost + graph[v][u])
            return

        path.append(v)
        for u in range(N):
            if u not in path:
                search(u, cost + graph[v][u])
        path.pop()

    # BEGIN
    search(v=0, cost=0)
    return min_cost


if __name__ == '__main__':
    print(solution(*params()))
