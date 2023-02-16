# 숫자 카드 2
# Silver IV
# https://www.acmicpc.net/problem/10816
from sys import stdin
from collections import Counter


def read_input():
    N = int(stdin.readline())
    cards = list(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    return N, cards, M, nums


def solve(N: int, cards: list[int], M: int, nums: list[int]):
    counter = Counter(cards)
    return [counter[num] for num in nums]


def print_output(counter: list[int]):
    print(' '.join(map(str, counter)))


if __name__ == '__main__':
    print_output(solve(*read_input()))
