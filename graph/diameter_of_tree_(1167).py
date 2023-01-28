# 트리의 지름
# Gold II
# https://www.acmicpc.net/problem/1167
from sys import stdin


def params():
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
    return V, graph


def solution(V: int, graph: list[tuple[int, int]]):
    def find_end(start: int):
        visited = set()
        end = 0
        dist_to_end = 0

        def search(v: int, dist: int):
            nonlocal dist_to_end
            if dist_to_end < dist:
                nonlocal end
                end = v
                dist_to_end = dist

            visited.add(v)
            for u, w in graph[v]:
                if u not in visited:
                    search(u, dist + w)

        # BEGIN
        search(v=start, dist=0)
        return end, dist_to_end

    # BEGIN
    one_end, _ = find_end(start=1)
    _, diameter = find_end(start=one_end)
    return diameter


if __name__ == '__main__':
    print(solution(*params()))
