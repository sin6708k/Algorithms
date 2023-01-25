# 연속합
# https://www.acmicpc.net/problem/1912
from sys import stdin


if __name__ == '__main__':
    N = int(stdin.readline())
    seq = list(map(int, stdin.readline().split()))
    sum_memo = [0] * N

    for i in range(N):
        sum_memo[i] = max(sum_memo[i - 1] + seq[i],
                          seq[i])

    print(max(sum_memo))
