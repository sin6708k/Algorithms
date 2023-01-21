# 트리의 지름
# https://www.acmicpc.net/problem/1167
from sys import stdin


def search(path: list[int], dist: int):
    global graph
    global end
    global max_dist
    v = path[-1]

    if max_dist < dist:
        end = v
        max_dist = dist

    for u, w in graph[v]:
        if u not in path:
            search(path + [u], dist + w)


if __name__ == '__main__':
    V = int(stdin.readline())
    graph = [[] for _ in range(V + 1)]  # v = 0 is unused

    for _ in range(V):
        input_iter = iter(map(int, stdin.readline().split()))
        v = next(input_iter)
        while True:
            u = next(input_iter)
            if u == -1:
                break
            w = next(input_iter)
            graph[v].append((u, w))

    max_dist = 0
    search([1], 0)
    max_dist = 0
    search([end], 0)
    print(max_dist)
