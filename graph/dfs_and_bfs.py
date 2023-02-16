# DFS와 BFS
# Silver II
# https://www.acmicpc.net/problem/1260
from sys import stdin
from collections import deque


def read_input():
    N, M, V = map(int, stdin.readline().split())
    graph = [[] for _ in range(N + 1)]  # v = 0 is unused

    for _ in range(M):
        v, u = map(int, stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)
    for edge in graph:
        edge.sort()
    return N, M, V, graph


def solve(N: int, M: int, V: int, graph: list[list[int]]):
    def dfs(start: int):
        visited = set()
        log = []

        def search(v: int):
            visited.add(v)
            log.append(v)

            for u in graph[v]:
                if u not in visited:
                    search(u)

        # BEGIN
        search(v=start)
        return log

    def bfs(start: int):
        visited = set()
        to_visit = deque([start])
        log = []

        while to_visit:
            v = to_visit.popleft()
            visited.add(v)
            log.append(v)
            to_visit.extend(u for u in graph[v]
                            if u not in visited
                            and u not in to_visit)
        return log

    # BEGIN
    return dfs(start=V), bfs(start=V)


def print_output(dfs_log: list[int], bfs_log: list[int]):
    print(' '.join(map(str, dfs_log)))
    print(' '.join(map(str, bfs_log)))


if __name__ == '__main__':
    print_output(*solve(*read_input()))
