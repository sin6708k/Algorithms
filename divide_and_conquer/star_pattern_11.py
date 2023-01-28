# 별 찍기 - 11
# Gold IV
# https://www.acmicpc.net/problem/2448
from sys import stdin


def solution(N: int):
    printing = [''] * N

    def margin():
        for y in range(N):
            printing[y] += ' ' * (N - y - 1)

    def triangle(h: int, y: int):
        if h == 3:
            printing[y] += '*'
            printing[y + 1] += '* *'
            printing[y + 2] += '*****'
            return

        h //= 2
        triangle(h, y)
        triangle(h, y + h)
        empty_inverted_triangle(h, y + h)
        triangle(h, y + h)

    def empty_triangle(h: int, y: int):
        if h == 3:
            printing[y] += ' '
            printing[y + 1] += '   '
            printing[y + 2] += '     '
            return

        h //= 2
        empty_triangle(h, y)
        empty_triangle(h, y + h)
        empty_inverted_triangle(h, y + h)
        empty_triangle(h, y + h)

    def empty_inverted_triangle(h: int, y: int):
        if h == 3:
            printing[y] += '     '
            printing[y + 1] += '   '
            printing[y + 2] += ' '
            return

        h //= 2
        empty_inverted_triangle(h, y)
        empty_triangle(h, y)
        empty_inverted_triangle(h, y)
        empty_inverted_triangle(h, y + h)

    # BEGIN
    margin()
    triangle(N, 0)
    margin()
    return '\n'.join(printing)


if __name__ == '__main__':
    print(solution(N=int(stdin.readline())))
