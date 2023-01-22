# 스도쿠
# https://www.acmicpc.net/problem/2239
from sys import stdin
from collections import deque


def can_place(value: int, x: int, y: int) -> bool:
    global table

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
    global table
    global empty_points

    if not empty_points:
        return True
    x, y = empty_points[0]

    for value in range(1, 10):
        if can_place(value, x, y):
            table[y][x] = value
            empty_points.popleft()
            if fill():
                return True
            table[y][x] = 0
            empty_points.appendleft((x, y))
    return False


if __name__ == '__main__':
    table = [list(map(int, stdin.readline().rstrip()))
             for _ in range(9)]
    empty_points = deque([(x, y)
                          for y in range(9) for x in range(9)
                          if table[y][x] == 0])

    fill()
    print('\n'.join(''.join(map(str, row))
                    for row in table))
