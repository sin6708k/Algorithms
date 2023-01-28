# 스도쿠
# Gold IV
# https://www.acmicpc.net/problem/2580
from sys import stdin


def solution(table: list[list[int]]):
    empty_cells = [(x, y)
                   for y in range(8, -1, -1)
                   for x in range(8, -1, -1)
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
    return '\n'.join(' '.join(map(str, row))
                     for row in table)


if __name__ == '__main__':
    print(solution(table=[list(map(int, stdin.readline().split()))
                          for _ in range(9)]))
