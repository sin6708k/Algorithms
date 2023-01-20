# Z
# https://www.acmicpc.net/problem/1074
from sys import stdin


def search_dist(h: int, x: int, y: int, dist: int) -> int:
    global R
    global C

    if h == 1:
        return dist

    h //= 2
    area = h ** 2
    if R < y + h:
        if C < x + h:
            return search_dist(h, x, y, dist)
        else:
            return search_dist(h, x + h, y, dist + area)
    else:
        if C < x + h:
            return search_dist(h, x, y + h, dist + area * 2)
        else:
            return search_dist(h, x + h, y + h, dist + area * 3)


if __name__ == '__main__':
    N, R, C = map(int, stdin.readline().split())
    H = 2 ** N

    print(search_dist(H, 0, 0, 0))
