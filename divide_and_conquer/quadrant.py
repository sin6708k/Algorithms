# 사분면
# https://www.acmicpc.net/problem/1891
from sys import stdin


def search_start(h: int, x: int, y: int) -> tuple:
    global token_iter

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
    global token_iter
    global x_f
    global y_f

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


if __name__ == '__main__':
    input_iter = iter(stdin.readline().split())
    D = int(next(input_iter))
    H = 2 ** D

    token_iter = iter(next(input_iter))
    x_i, y_i = search_start(H, 0, 0)

    DX, DY = map(int, stdin.readline().split())
    x_f = x_i + DX
    y_f = y_i - DY

    if x_f < 0 or x_f >= H:
        print(-1)
    elif y_f < 0 or y_f >= H:
        print(-1)
    else:
        print(search_index(H, 0, 0, ''))
