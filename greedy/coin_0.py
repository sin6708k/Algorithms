# 동전 0
# Silver IV
# https://www.acmicpc.net/problem/11047
from sys import stdin
from heapq import heapify, heappop


def params():
    N, K = map(int, stdin.readline().split())
    coins = [(-coin, coin)
             for coin in (int(stdin.readline())
                          for _ in range(N))]
    heapify(coins)
    return N, K, coins


def solution(N: int, K: int, coins: list[tuple[int, int]]):
    count = 0
    money = K

    while coins and money > 0:
        _, coin = heappop(coins)
        count_of_coin = money // coin
        count += count_of_coin
        money -= coin * count_of_coin
    return count


if __name__ == '__main__':
    print(solution(*params()))
