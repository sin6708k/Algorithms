# 음계
# https://www.acmicpc.net/problem/2920
from sys import stdin


if __name__ == '__main__':
    nums = list(map(int, stdin.readline().split()))
    first = nums[0]

    if first == 1:
        if all(i == num
               for i, num in enumerate(nums, 1)):
            print('ascending')
        else:
            print('mixed')
    elif first == 8:
        if all(i == num
               for i, num in enumerate(reversed(nums), 1)):
            print('descending')
        else:
            print('mixed')
    else:
        print('mixed')
