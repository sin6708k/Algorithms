# 별 찍기 - 10
# https://www.acmicpc.net/problem/2447
from sys import stdin


def rect(h: int, y: int):
    global printing

    if h == 3:
        printing[y] += '***'
        printing[y + 1] += '* *'
        printing[y + 2] += '***'
        return

    h //= 3
    for _ in range(3):
        rect(h, y)
    rect(h, y + h)
    empty_rect(h, y + h)
    rect(h, y + h)
    for _ in range(3):
        rect(h, y + h * 2)


def empty_rect(h: int, y: int):
    global printing

    if h == 3:
        for i in range(3):
            printing[y + i] += '   '
        return

    h //= 3
    for i in range(3):
        for _ in range(3):
            empty_rect(h, y + h * i)


if __name__ == '__main__':
    N = int(stdin.readline())
    printing = [''] * N

    rect(N, 0)
    print('\n'.join(printing))
