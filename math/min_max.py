# 최소, 최대
# https://www.acmicpc.net/problem/10818
from sys import stdin


if __name__ == '__main__':
    N = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))

    print(min(nums), max(nums))
