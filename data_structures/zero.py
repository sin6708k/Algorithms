# 제로
# Silver IV
# https://www.acmicpc.net/problem/10773
from sys import stdin


def params():
    K = int(stdin.readline())
    nums = [int(stdin.readline())
            for _ in range(K)]
    return K, nums


def solution(N: int, nums: list[int]):
    stack = []
    for num in nums:
        if num != 0:
            stack.append(num)
        else:
            stack.pop()
    return sum(stack)


if __name__ == '__main__':
    print(solution(*params()))
