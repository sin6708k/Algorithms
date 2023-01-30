# 조합
# Silver III
# https://www.acmicpc.net/problem/2407
from sys import stdin
from math import comb


def params():
    N, M = map(int, stdin.readline().split())
    return N, M


def solution(N: int, M: int):
    return comb(N, M)


if __name__ == '__main__':
    print(solution(*params()))
