# 연속합
# Silver II
# https://www.acmicpc.net/problem/1912
from sys import stdin


def read_input():
    N = int(stdin.readline())
    seq = list(map(int, stdin.readline().split()))
    return N, seq


def solve(N: int, seq: list[int]):
    prefix_sum = [0] * N
    for i in range(N):
        prefix_sum[i] = max(prefix_sum[i - 1] + seq[i], seq[i])
    return max(prefix_sum)


if __name__ == '__main__':
    print(solve(*read_input()))
