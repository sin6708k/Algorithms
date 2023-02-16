# N-Queen
# Gold IV
# https://www.acmicpc.net/problem/9663
from sys import stdin


def read_input():
    return int(stdin.readline())


def solve(N: int):
    placed_on_cols = set()
    board = [0] * N
    count = 0

    def can_place(x: int, y: int) -> bool:
        if x in placed_on_cols:
            return False
        for i in range(y):
            if abs(x - board[i]) == abs(y - i):
                return False
        return True

    def place(y: int):
        if y == N:
            nonlocal count
            count += 1
            return

        for x in range(N):
            if can_place(x, y):
                placed_on_cols.add(x)
                board[y] = x
                place(y + 1)
                placed_on_cols.remove(x)

    # BEGIN
    place(y=0)
    return count


if __name__ == '__main__':
    print(solve(read_input()))
