# 동전 0
# Silver IV
# https://www.acmicpc.net/problem/11047
from sys import stdin
from heapq import heapify, heappop


def read_input():
    N, K = map(int, stdin.readline().split())
    coins = [-int(stdin.readline())
             for _ in range(N)]
    heapify(coins)
    return N, K, coins


def solve(N: int, K: int, coins: list[int]):
    count = 0
    money = K

    while coins and money > 0:
        coin = -heappop(coins)
        count_of_coin = money // coin
        count += count_of_coin
        money -= coin * count_of_coin
    return count


if __name__ == '__main__':
    print(solve(*read_input()))
