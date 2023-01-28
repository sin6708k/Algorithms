# 배열 합치기
# Silver V
# https://www.acmicpc.net/problem/11728
from sys import stdin


def params():
    N, M = map(int, stdin.readline().split())
    one_nums = list(map(int, stdin.readline().split()))
    another_nums = list(map(int, stdin.readline().split()))
    return N, M, one_nums, another_nums


def solution(N: int, M: int, one_nums: list[int], another_nums: list[int]):
    i = 0
    j = 0
    nums = []

    while True:
        if i == N:
            nums.extend(another_nums[j:])
            break
        if j == M:
            nums.extend(one_nums[i:])
            break

        if one_nums[i] < another_nums[j]:
            nums.append(one_nums[i])
            i += 1
        else:
            nums.append(another_nums[j])
            j += 1

    return ' '.join(map(str, nums))


if __name__ == '__main__':
    print(solution(*params()))
