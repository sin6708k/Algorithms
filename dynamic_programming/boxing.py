# 상자넣기
# Silver II
# https://www.acmicpc.net/problem/1965
from sys import stdin


def read_input():
    N = int(stdin.readline())
    boxes = list(map(int, stdin.readline().split()))
    return N, boxes


def solve(N: int, boxes: list[int]):
    count = [0] * N
    for i in range(N):
        count[i] = max((count[j] + 1
                        for j in range(i)
                        if boxes[j] < boxes[i]),
                       default=1)
    return max(count)


if __name__ == '__main__':
    print(solve(*read_input()))
