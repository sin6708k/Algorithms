# Z
# Silver I
# https://www.acmicpc.net/problem/1074
from sys import stdin


def read_input():
    N, R, C = map(int, stdin.readline().split())
    return N, R, C


def solve(N: int, R: int, C: int):
    H = 2 ** N

    def find_dist(h: int, x: int, y: int, dist: int) -> int:
        if h == 1:
            return dist

        h //= 2
        area = h ** 2
        if R < y + h:
            if C < x + h:
                return find_dist(h, x, y, dist)
            else:
                return find_dist(h, x + h, y, dist + area)
        else:
            if C < x + h:
                return find_dist(h, x, y + h, dist + area * 2)
            else:
                return find_dist(h, x + h, y + h, dist + area * 3)

    # BEGIN
    return find_dist(H, 0, 0, 0)


if __name__ == '__main__':
    print(solve(*read_input()))
