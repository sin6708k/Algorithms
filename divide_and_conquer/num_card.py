# 숫자 카드
# Silver V
# https://www.acmicpc.net/problem/10815
from sys import stdin


def read_input():
    N = int(stdin.readline())
    cards = sorted(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    return N, cards, M, nums


# Implemented with binary search
def solve(N: int, cards: list[int], M: int, nums: list[int]):
    def exist(num: int, left: int, right: int) -> bool:
        if left >= right:
            return False
        mid = (left + right) // 2

        if num == cards[mid]:
            return True
        elif num < cards[mid]:
            return exist(num, left, mid)
        else:
            return exist(num, mid + 1, right)

    # BEGIN
    return [exist(num, 0, N)
            for num in nums]


def print_output(nums_exist: list[bool]):
    print(' '.join(map(str, map(int, nums_exist))))


if __name__ == '__main__':
    print_output(solve(*read_input()))
