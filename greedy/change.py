# 거스름돈
# https://www.acmicpc.net/problem/5585
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
    PRICE = int(stdin.readline())
    PAY = 1000
    MONEY = PAY - PRICE
    coin_iter = iter([500, 100, 50, 10, 5, 1])

    print(count_coin(MONEY))
