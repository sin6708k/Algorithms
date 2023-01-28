# 거스름돈
# Bronze II
# https://www.acmicpc.net/problem/5585
from sys import stdin


def solution(PRICE: int):
    PAY = 1000
    count = 0
    money = PAY - PRICE
    coins = [1, 5, 10, 50, 100, 500]

    while coins and money > 0:
        coin = coins.pop()
        count_of_coin = money // coin
        count += count_of_coin
        money -= coin * count_of_coin
    return count


if __name__ == '__main__':
    print(solution(PRICE=int(stdin.readline())))
