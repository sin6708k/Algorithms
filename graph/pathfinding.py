# 경로 찾기
# Silver I
# https://www.acmicpc.net/problem/11403
from sys import stdin


def params():
    N = int(stdin.readline())
    graph = [list(map(int, stdin.readline().split()))
             for _ in range(N)]
    return N, graph


def solution(N: int, graph: list[list[int]]):
    connected = [[0] * N
                 for _ in range(N)]

    def find_path(start: int, v: int):
        for u in range(N):
            if graph[v][u] == 0 or connected[start][u] == 1:
                continue
            connected[start][u] = 1
            find_path(start, u)

    def find_all_paths():
        for v in range(N):
            find_path(v, v)

    # BEGIN
    find_all_paths()
    return '\n'.join(' '.join(map(str, (w for w in edge)))
                     for edge in connected)


if __name__ == '__main__':
    print(solution(*params()))
