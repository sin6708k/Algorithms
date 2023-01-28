# 설탕 배달
# Silver IV
# https://www.acmicpc.net/problem/2839
from sys import stdin


def solution(N: int):
    count = [0] + [10 ** 9] * N
    for i in range(3, N + 1):
        count[i] = min(count[i - 3] + 1,
                       count[i - 5] + 1)

    return count[-1] if count[-1] <= 10 ** 9 else -1


if __name__ == '__main__':
    print(solution(N=int(stdin.readline())))
