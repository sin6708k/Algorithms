# 스도쿠
# https://www.acmicpc.net/problem/2580
from sys import stdin


def can_place(cell: int, x: int, y: int) -> bool:
    global table

    if cell in table[y]:
        return False
    for i in range(9):
        if cell == table[i][x]:
            return False

    top = y // 3 * 3
    left = x // 3 * 3

    for i in range(top, top + 3):
        for j in range(left, left + 3):
            if cell == table[i][j]:
                return False

    return True


def fill(empty_points: list[tuple]) -> bool:
    global table
    n = len(empty_points)

    if n == 0:
        return True

    x, y = empty_points[0]

    for cell in range(1, 10):
        if can_place(cell, x, y):
            table[y][x] = cell
            if fill(empty_points[1:]):
                return True
            table[y][x] = 0

    return False


if __name__ == '__main__':
    table = [list(map(int, stdin.readline().split()))
             for _ in range(9)]
    empty_points = [(x, y)
                    for y in range(9) for x in range(9)
                    if table[y][x] == 0]

    fill(empty_points)
    print('\n'.join(' '.join(map(str, row))
                    for row in table))
