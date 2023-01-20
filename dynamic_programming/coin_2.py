# 동전 2
# https://www.acmicpc.net/problem/2294
from sys import stdin


if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    coins = {int(stdin.readline())
             for _ in range(N)}
    count_memo = [0] * (K + 1)

    for i in range(1, K + 1):
        count_memo[i] = min((count + 1
                             for j, count in enumerate(count_memo[:i])
                             if i - j in coins),
                            default=K + 1)

    print(count_memo[K] if count_memo[K] <= K else -1)
