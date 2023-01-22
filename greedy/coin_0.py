# 동전 0
# https://www.acmicpc.net/problem/11047
from sys import stdin
from heapq import heapify, heappop


def count_coin(money: int) -> int:
    global coins

    if money == 0:
        return 0

    _, coin = heappop(coins)
    if coin > money:
        return count_coin(money)

    count = money // coin
    return count_coin(money - coin * count) + count


if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    coins = [(-coin, coin)
             for coin in (int(stdin.readline())
                          for _ in range(N))]
    heapify(coins)

    print(count_coin(K))
