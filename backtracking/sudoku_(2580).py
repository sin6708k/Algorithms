# 스도쿠
# Gold IV
# https://www.acmicpc.net/problem/2580
from sys import stdin
from itertools import product


def read_input():
    return [list(map(int, stdin.readline().split()))
            for _ in range(9)]


def solve(table: list[list[int]]) -> list[list[int]]:
    empty_cells = [(x, y)
                   for y, x in product(range(8, -1, -1), repeat=2)
                   if table[y][x] == 0]

    def can_place(value: int, x: int, y: int) -> bool:
        if value in table[y]:
            return False
        for i in range(9):
            if value == table[i][x]:
                return False

        top = y // 3 * 3
        left = x // 3 * 3
        for i in range(top, top + 3):
            for j in range(left, left + 3):
                if value == table[i][j]:
                    return False
        return True

    def fill() -> bool:
        if not empty_cells:
            return True
        x, y = empty_cells.pop()

        for value in range(1, 10):
            if can_place(value, x, y):
                table[y][x] = value
                if fill():
                    return True
                table[y][x] = 0

        empty_cells.append((x, y))
        return False

    # BEGIN
    fill()
    return table


def print_output(table: list[list[int]]):
    print('\n'.join(' '.join(map(str, row))
                    for row in table))


if __name__ == '__main__':
    print_output(solve(read_input()))
