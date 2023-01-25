# 최댓값
# https://www.acmicpc.net/problem/2562
from sys import stdin


if __name__ == '__main__':
    N = 9
    nums = [int(stdin.readline())
            for _ in range(N)]
    max_num, index = max((num, i)
                         for i, num in enumerate(nums, 1))

    print(max_num)
    print(index)
