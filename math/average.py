# 평균
# https://www.acmicpc.net/problem/1546
from sys import stdin


if __name__ == '__main__':
    N = int(stdin.readline())
    scores = list(map(int, stdin.readline().split()))
    M = max(scores)

    print(sum(scores) / M * 100 / N)
