# 동전 0
# https://www.acmicpc.net/problem/11047
from sys import stdin


def count_coin(money: int) -> int:
    global coin_iter

    if money == 0:
        return 0

    coin = next(coin_iter)
    if coin > money:
        return count_coin(money)

    count = money // coin
    return count_coin(money - coin * count) + count


if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    coin_iter = iter(sorted([int(stdin.readline())
                             for _ in range(N)],
                            reverse=True))

    print(count_coin(K))
