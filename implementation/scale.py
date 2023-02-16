# 음계
# Bronze II
# https://www.acmicpc.net/problem/2920
from sys import stdin


def read_input():
    return list(map(int, stdin.readline().split()))


def solve(nums: list[int]):
    if nums[0] == 1:
        if all(i == num for i, num in enumerate(nums, 1)):
            return 'ascending'
        else:
            return 'mixed'
    elif nums[0] == 8:
        if all(i == num for i, num in enumerate(reversed(nums), 1)):
            return 'descending'
        else:
            return 'mixed'
    else:
        return 'mixed'


if __name__ == '__main__':
    print(solve(read_input()))
