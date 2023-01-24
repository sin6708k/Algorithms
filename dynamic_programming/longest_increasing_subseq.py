# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
from sys import stdin
from itertools import islice


if __name__ == '__main__':
    N = int(stdin.readline())
    seq = list(map(int, stdin.readline().split()))
    count_memo = [0] * N

    for i in range(N):
        count_memo[i] = max((count_memo[j] + 1
                             for j in range(i)
                             if seq[j] < seq[i]),
                            default=1)

    print(max(count_memo))
