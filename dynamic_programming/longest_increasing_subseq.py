# 가장 긴 증가하는 부분 수열
# Silver II
# https://www.acmicpc.net/problem/11053
from sys import stdin


def read_input():
    N = int(stdin.readline())
    seq = list(map(int, stdin.readline().split()))
    return N, seq


def solve(N: int, seq: list[int]):
    count = [0] * N
    for i in range(N):
        count[i] = max((count[j] + 1
                        for j in range(i)
                        if seq[j] < seq[i]),
                       default=1)
    return max(count)


if __name__ == '__main__':
    print(solve(*read_input()))
