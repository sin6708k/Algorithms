# 사분면
# Gold IV
# https://www.acmicpc.net/problem/1891
from sys import stdin


def params():
    D, INDEX = map(int, stdin.readline().split())
    DX, DY = map(int, stdin.readline().split())
    return D, INDEX, DX, DY


def solution(D: int, INDEX: int, DX: int, DY: int):
    token_iter = iter(str(INDEX))
    H = 2 ** D

    def search_start(h: int, x: int, y: int) -> tuple:
        if h == 1:
            return x, y

        token = next(token_iter)
        h //= 2
        if token == '2':
            return search_start(h, x, y)
        if token == '1':
            return search_start(h, x + h, y)
        if token == '3':
            return search_start(h, x, y + h)
        if token == '4':
            return search_start(h, x + h, y + h)

    def search_index(h: int, x: int, y: int, index: str) -> str:
        if h == 1:
            return index

        h //= 2
        if y_f < y + h:
            if x_f < x + h:
                return search_index(h, x, y, index + '2')
            else:
                return search_index(h, x + h, y, index + '1')
        else:
            if x_f < x + h:
                return search_index(h, x, y + h, index + '3')
            else:
                return search_index(h, x + h, y + h, index + '4')

    # BEGIN
    x_i, y_i = search_start(H, 0, 0)
    x_f = x_i + DX
    y_f = y_i + DY

    if x_f < 0 or x_f >= H:
        return '-1'
    if y_f < 0 or y_f >= H:
        return '-1'

    return search_index(H, 0, 0, '')


if __name__ == '__main__':
    print(solution(*params()))
