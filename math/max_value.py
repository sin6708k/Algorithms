# 최댓값
# Bronze III
# https://www.acmicpc.net/problem/2562
from sys import stdin


def solution(nums: list[int]):
    return '\n'.join(map(str, max((num, i)
                                  for i, num in enumerate(nums, 1))))


if __name__ == '__main__':
    print(solution(nums=[int(stdin.readline())
                         for _ in range(9)]))
