# DFS와 BFS
# https://www.acmicpc.net/problem/1260
from sys import stdin
from collections import deque


def dfs(v: int):
    global graph
    global visited
    visited.add(v)
    print(v, end=' ')

    for u in graph[v]:
        if u not in visited:
            dfs(u)


def bfs(v: int):
    global graph
    global visited
    global to_visit
    visited.add(v)
    print(v, end=' ')

    to_visit.extend(u for u in graph[v]
                    if u not in visited
                    and u not in to_visit)

    if to_visit:
        bfs(to_visit.popleft())


if __name__ == '__main__':
    N, M, V = map(int, stdin.readline().split())
    graph = [[] for _ in range(N + 1)]  # v = 0 is unused

    for _ in range(M):
        v, u = map(int, stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)
    for edge in graph:
        edge.sort()

    visited = set()
    dfs(V)
    print()

    visited.clear()
    to_visit = deque()
    bfs(V)
