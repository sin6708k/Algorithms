# 이항 계수 1
# Bronze I
# https://www.acmicpc.net/problem/11050
from sys import stdin
from math import comb


def params():
    N, K = map(int, stdin.readline().split())
    return N, K


def solution(N: int, K: int):
    return comb(N, K)


if __name__ == '__main__':
    print(solution(*params()))
