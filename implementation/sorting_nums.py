# 수 정렬하기
# Bronze II
# https://www.acmicpc.net/problem/2750
from sys import stdin


def read_input():
    N = int(stdin.readline())
    nums = [int(stdin.readline())
            for _ in range(N)]
    return N, nums


# Implemented with insertion sort
def solve(N: int, nums: list[int]):
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[j + 1]:
                break
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def print_output(nums: list[int]):
    print('\n'.join(map(str, nums)))


if __name__ == '__main__':
    print_output(solve(*read_input()))
