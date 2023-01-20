# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
from sys import stdin


def merge_sort(nums: list[int]) -> list[int]:
    n = len(nums)

    if n == 1:
        return nums

    mid = n // 2

    left_nums = merge_sort(nums[:mid])
    right_nums = merge_sort(nums[mid:])
    return merge(left_nums, right_nums)


def merge(left_nums: list[int], right_nums: list[int]) -> list[int]:
    n = len(left_nums)
    m = len(right_nums)
    i = 0
    j = 0
    nums = []

    while True:
        if i == n:
            nums.extend(right_nums[j:])
            break
        if j == m:
            nums.extend(left_nums[i:])
            break

        if left_nums[i] < right_nums[j]:
            nums.append(left_nums[i])
            i += 1
        else:
            nums.append(right_nums[j])
            j += 1

    return nums


if __name__ == '__main__':
    N = int(stdin.readline())
    nums = [int(stdin.readline())
            for _ in range(N)]

    print('\n'.join(map(str,
                        merge_sort(nums))))
