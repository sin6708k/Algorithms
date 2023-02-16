# 수 찾기
# Silver IV
# https://www.acmicpc.net/problem/1920
from sys import stdin


def read_input():
    N = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    nums_to_find = list(map(int, stdin.readline().split()))
    return N, nums, M, nums_to_find


# Implemented with binary search
def solve(N: int, nums: list[int], M: int, nums_to_find: list[int]):
    def exist(num_to_find: int, left: int, right: int) -> bool:
        if left >= right:
            return False
        mid = (left + right) // 2

        if num_to_find == nums[mid]:
            return True
        elif num_to_find < nums[mid]:
            return exist(num_to_find, left, mid)
        else:
            return exist(num_to_find, mid + 1, right)

    # BEGIN
    nums.sort()
    return [exist(num_to_find, 0, N)
            for num_to_find in nums_to_find]


def print_output(nums_exist: list[bool]):
    print('\n'.join(map(str, map(int, nums_exist))))


if __name__ == '__main__':
    print_output(solve(*read_input()))
