# 설탕 배달
# https://www.acmicpc.net/problem/2839
from sys import stdin


if __name__ == '__main__':
    N = int(stdin.readline())
    count_memo = [0] + [N + 1] * N

    for i in range(3, N + 1):
        count_memo[i] = min(count_memo[i - 3] + 1,
                            count_memo[i - 5] + 1)

    print(count_memo[N] if count_memo[N] <= N else -1)
