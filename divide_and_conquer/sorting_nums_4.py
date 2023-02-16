# 수 정렬하기 4
# Silver V
# https://www.acmicpc.net/problem/11931
from sys import stdin


def read_input():
    N = int(stdin.readline())
    all_nums = [int(stdin.readline())
                for _ in range(N)]
    return N, all_nums


# Implemented by merge sort
def solve(N: int, all_nums: list[int]):
    def merge(left_nums: list[int], right_nums: list[int]) -> list[int]:
        i = 0
        j = 0
        nums = []

        while True:
            if i == len(left_nums):
                nums.extend(right_nums[j:])
                break
            if j == len(right_nums):
                nums.extend(left_nums[i:])
                break

            if left_nums[i] >= right_nums[j]:
                nums.append(left_nums[i])
                i += 1
            else:
                nums.append(right_nums[j])
                j += 1
        return nums

    def sort(nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        return merge(sort(nums[:mid]), sort(nums[mid:]))

    # BEGIN
    return sort(all_nums)


def print_output(nums: list[int]):
    print('\n'.join(map(str, nums)))


if __name__ == '__main__':
    print_output(solve(*read_input()))
