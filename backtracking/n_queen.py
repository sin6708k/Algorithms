# N-Queen
# https://www.acmicpc.net/problem/9663
from sys import stdin


def can_place(x: int, y: int) -> bool:
    if x in placed_on_cols:
        return False
    if any(abs(x - board[i]) == (abs(y - i)) for i in range(y)):
        return False
    return True


def place(y: int):
    global N
    global placed_on_cols
    global board
    global count

    if y == N:
        count += 1
        return

    for x in range(N):
        if can_place(x, y):
            placed_on_cols.add(x)
            board[y] = x
            place(y + 1)
            placed_on_cols.remove(x)


if __name__ == '__main__':
    N = int(stdin.readline())
    placed_on_cols = set()
    board = [0] * N
    count = 0

    place(0)
    print(count)
