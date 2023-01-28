# 숫자 카드 2
# Silver IV
# https://www.acmicpc.net/problem/10816
from sys import stdin
from collections import Counter


def params():
    N = int(stdin.readline())
    cards = list(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    return N, cards, M, nums


def solution(N: int, cards: list[int], M: int, nums: list[int]):
    counter = Counter(cards)
    return ' '.join(map(str, (counter[num]
                              for num in nums)))


if __name__ == '__main__':
    print(solution(*params()))
