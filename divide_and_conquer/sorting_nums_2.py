# 수 정렬하기 2
# Silver V
# https://www.acmicpc.net/problem/2751
from sys import stdin


def params():
    N = int(stdin.readline())
    all_nums = [int(stdin.readline())
                for _ in range(N)]
    return N, all_nums


# Implemented by merge sort
def solution(N: int, all_nums: list[int]):
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
    return '\n'.join(map(str, sort(all_nums)))


if __name__ == '__main__':
    print(solution(*params()))
