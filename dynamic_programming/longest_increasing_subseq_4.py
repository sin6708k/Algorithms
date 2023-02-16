# 가장 긴 증가하는 부분 수열 4
# Gold IV
# https://www.acmicpc.net/problem/14002
from sys import stdin


def read_input():
    N = int(stdin.readline())
    seq = list(map(int, stdin.readline().split()))
    return N, seq


def solve(N: int, seq: list[int]):
    memo = [(0, [])] * N
    for i in range(N):
        memo[i] = max(((memo[j][0] + 1, memo[j][1] + [seq[i]])
                       for j in range(i)
                       if seq[j] < seq[i]),
                      default=(1, [seq[i]]))

    count, subseq = max(memo)
    return '\n'.join([str(count), ' '.join(map(str, subseq))])


if __name__ == '__main__':
    print(solve(*read_input()))
