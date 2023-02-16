# 경로 찾기
# Silver I
# https://www.acmicpc.net/problem/11403
from sys import stdin


def read_input():
    N = int(stdin.readline())
    graph = [list(map(bool, map(int, stdin.readline().split())))
             for _ in range(N)]
    return N, graph


def solve(N: int, graph: list[list[bool]]):
    connected = [[False] * N
                 for _ in range(N)]

    def find_path(start: int, v: int):
        for u in range(N):
            if not graph[v][u] or connected[start][u]:
                continue
            connected[start][u] = True
            find_path(start, u)

    def find_all_paths():
        for v in range(N):
            find_path(v, v)

    # BEGIN
    find_all_paths()
    return connected


def print_output(connected: list[list[bool]]):
    print('\n'.join(' '.join(map(str, map(int, edge)))
                    for edge in connected))


if __name__ == '__main__':
    print_output(solve(*read_input()))
