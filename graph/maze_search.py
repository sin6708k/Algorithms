# 미로 탐색
# Silver I
# https://www.acmicpc.net/problem/2178
from sys import stdin
from collections import deque


def read_input():
    N, M = map(int, stdin.readline().split())
    maze = [list(map(bool, map(int, stdin.readline().rstrip())))
            for _ in range(N)]
    return N, M, maze


def solve(N: int, M: int, maze: list[list[bool]]):
    maze = [[False] * (M + 2)] + [[False] + row + [False]
                                  for row in maze] + [[False] * (M + 2)]
    visited = [[False] * (M + 2)
               for _ in range(N + 2)]
    to_visit = deque([(1, 1, 1)])
    dist = 0

    while to_visit:
        x, y, dist = to_visit.popleft()

        if x == M and y == N:
            break
        if not maze[y][x]:
            continue
        if visited[y][x]:
            continue

        visited[y][x] = True
        to_visit.extend([(x - 1, y, dist + 1), (x + 1, y, dist + 1),
                         (x, y - 1, dist + 1), (x, y + 1, dist + 1)])
    return dist


if __name__ == '__main__':
    print(solve(*read_input()))
