# 평균
# Bronze I
# https://www.acmicpc.net/problem/1546
from sys import stdin


def params():
    N = int(stdin.readline())
    scores = list(map(int, stdin.readline().split()))
    return N, scores


def solution(N: int, scores: list[int]):
    return sum(scores) / max(scores) * 100 / N


if __name__ == '__main__':
    print(solution(*params()))
