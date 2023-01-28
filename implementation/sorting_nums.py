# 수 정렬하기
# Bronze II
# https://www.acmicpc.net/problem/2750
from sys import stdin


def params():
    N = int(stdin.readline())
    nums = [int(stdin.readline())
            for _ in range(N)]
    return N, nums


# Implemented with insertion sort
def solution(N: int, nums: list[int]):
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[j + 1]:
                break
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return '\n'.join(map(str, nums))


if __name__ == '__main__':
    print(solution(*params()))
