# 최소, 최대
# Bronze III
# https://www.acmicpc.net/problem/10818
from sys import stdin


def read_input():
    N = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    return N, nums


def solve(N: int, nums: list[int]):
    return min(nums), max(nums)


def print_output(min_num: int, max_num: int):
    print(min_num, max_num)


if __name__ == '__main__':
    print_output(*solve(*read_input()))
