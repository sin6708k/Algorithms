# K번째 수
# Silver V
# https://www.acmicpc.net/problem/11004
from sys import stdin


def read_input():
    N, K = map(int, stdin.readline().split())
    all_nums = list(map(int, stdin.readline().split()))
    return N, K, all_nums


# Implemented with merge sort
def solve(N: int, K: int, all_nums: list[int]):
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

            if left_nums[i] < right_nums[j]:
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
    return sort(all_nums)[K - 1]


if __name__ == '__main__':
    print(solve(*read_input()))
