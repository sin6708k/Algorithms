# 숫자 카드
# Silver V
# https://www.acmicpc.net/problem/10815
from sys import stdin


def params():
    N = int(stdin.readline())
    cards = sorted(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    return N, cards, M, nums


# Implemented with binary search
def solution(N: int, cards: list[int], M: int, nums: list[int]):
    def exist(num: int, left: int, right: int) -> int:
        if left >= right:
            return 0
        mid = (left + right) // 2

        if num == cards[mid]:
            return 1
        elif num < cards[mid]:
            return exist(num, left, mid)
        else:
            return exist(num, mid + 1, right)

    # BEGIN
    return ' '.join(map(str, (exist(num, 0, N)
                              for num in nums)))


if __name__ == '__main__':
    print(solution(*params()))
