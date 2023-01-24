# 경로 찾기
# https://www.acmicpc.net/problem/11403
from sys import stdin


def search(start: int, v: int):
    global visited

    for u in range(N):
        if graph[v][u] == 0:
            continue
        if visited[start][u] == 1:
            continue
        visited[start][u] = 1
        search(start, u)


if __name__ == '__main__':
    N = int(stdin.readline())
    graph = [list(map(int, stdin.readline().split()))
             for _ in range(N)]
    visited = [[0] * N
               for _ in range(N)]

    for v in range(N):
        search(v, v)

    print('\n'.join(' '.join(map(str,
                                 (w for w in edge)))
                    for edge in visited))
