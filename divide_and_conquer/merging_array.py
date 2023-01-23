# 배열 합치기
# https://www.acmicpc.net/problem/11728
from sys import stdin


def merge() -> list[int]:
    global left_nums
    global right_nums
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
    N, M = map(int, stdin.readline().split())
    left_nums = list(map(int, stdin.readline().split()))
    right_nums = list(map(int, stdin.readline().split()))

    print(' '.join(map(str, merge())))
