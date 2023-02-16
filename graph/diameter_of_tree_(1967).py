# 트리의 지름
# Gold IV
# https://www.acmicpc.net/problem/1967
from sys import stdin
from collections import deque


def read_input():
    N = int(stdin.readline())
    graph = [[] for _ in range(N + 1)]  # v = 0 is unused

    for _ in range(N - 1):
        v, u, w = map(int, stdin.readline().split())
        graph[v].append((u, w))
        graph[u].append((v, w))
    return N, graph


def solve(N: int, graph: list[tuple[int, int]]):
    def find_end(start: int):
        visited = set()
        to_visit = deque([(start, 0)])
        end = 0
        dist_to_end = 0

        while to_visit:
            v, dist = to_visit.popleft()
            if dist_to_end < dist:
                end = v
                dist_to_end = dist

            visited.add(v)
            to_visit.extend((u, dist + w)
                            for u, w in graph[v]
                            if u not in visited
                            and u not in to_visit)
        return end, dist_to_end

    # BEGIN
    one_end, _ = find_end(start=1)
    _, diameter = find_end(start=one_end)
    return diameter


if __name__ == '__main__':
    print(solve(*read_input()))
