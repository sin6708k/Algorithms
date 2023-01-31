# 수 찾기
# Silver IV
# https://www.acmicpc.net/problem/1920
from sys import stdin


def params():
    N = int(stdin.readline())
    nums = sorted(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    to_find = list(map(int, stdin.readline().split()))
    return N, nums, M, to_find


# Implemented with binary search
def solution(N: int, nums: list[int], M: int, nums_to_find: list[int]):
    def exist(num_to_find: int, left: int, right: int) -> int:
        if left >= right:
            return 0
        mid = (left + right) // 2

        if num_to_find == nums[mid]:
            return 1
        elif num_to_find < nums[mid]:
            return exist(num_to_find, left, mid)
        else:
            return exist(num_to_find, mid + 1, right)

    # BEGIN
    return '\n'.join(map(str, (exist(num_to_find, 0, N)
                              for num_to_find in nums_to_find)))


if __name__ == '__main__':
    print(solution(*params()))
