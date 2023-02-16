# 풍선 맞추기
# 골드 V
# https://www.acmicpc.net/problem/11509
from sys import stdin


def read_input():
    N = int(stdin.readline())
    balloons = list(map(int, stdin.readline().split()))
    return N, balloons


def solve(N: int, balloons: list[int]):
    arrows = [0] * 1000001

    for h in balloons:
        if arrows[h] > 0:
            arrows[h] -= 1
        arrows[h - 1] += 1
    return sum(arrows)


if __name__ == '__main__':
    print(solve(*read_input()))
