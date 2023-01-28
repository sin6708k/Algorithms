# 최소, 최대
# Bronze III
# https://www.acmicpc.net/problem/10818
from sys import stdin


def params():
    N = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    return N, nums


def solution(N: int, nums: list[int]):
    return ' '.join(map(str, [min(nums), max(nums)]))


if __name__ == '__main__':
    print(solution(*params()))
