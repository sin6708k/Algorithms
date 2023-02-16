# 최댓값
# Bronze III
# https://www.acmicpc.net/problem/2562
from sys import stdin


def read_input():
    return [int(stdin.readline())
            for _ in range(9)]


def solve(nums: list[int]):
    return max((num, i)
               for i, num in enumerate(nums, 1))


def print_output(max_num: int, index: int):
    print(max_num)
    print(index)


if __name__ == '__main__':
    print_output(*solve(read_input()))
