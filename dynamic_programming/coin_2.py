# 동전 2
# Gold V
# https://www.acmicpc.net/problem/2294
from sys import stdin


def read_input():
    N, K = map(int, stdin.readline().split())
    coins = {int(stdin.readline())
             for _ in range(N)}
    return N, K, coins


def solve(N: int, K: int, coins: set[int]):
    count = [0] * (K + 1)
    for i in range(1, K + 1):
        count[i] = min((count[j] + 1
                        for j in range(i)
                        if i - j in coins),
                       default=10 ** 9)
    return count[-1] if count[-1] <= 10 ** 9 else -1


if __name__ == '__main__':
    print(solve(*read_input()))
