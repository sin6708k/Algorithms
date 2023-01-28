# DFS와 BFS
# Silver II
# https://www.acmicpc.net/problem/1260
from sys import stdin
from collections import deque


def params():
    N, M, V = map(int, stdin.readline().split())
    graph = [[] for _ in range(N + 1)]  # v = 0 is unused

    for _ in range(M):
        v, u = map(int, stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)
    for edge in graph:
        edge.sort()
    return N, M, V, graph


def solution(N: int, M: int, V: int, graph: list[list[int]]):
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
        return ' '.join(map(str, log))

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
        return ' '.join(map(str, log))

    # BEGIN
    return '\n'.join([dfs(start=V), bfs(start=V)])


if __name__ == '__main__':
    print(solution(*params()))
