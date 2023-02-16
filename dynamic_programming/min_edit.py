# 최소 편집
# Gold III
# https://www.acmicpc.net/problem/15483
from sys import stdin
from itertools import product


def read_input():
    A = stdin.readline()
    B = stdin.readline()
    return A, B


def solve(A: str, B: str):
    dist = [[i if j == 0 else
             j if i == 0 else
             0 for j in range(len(B) + 1)]
            for i in range(len(A) + 1)]

    for i, j in product(range(1, len(A) + 1), range(1, len(B) + 1)):
        dist[i][j] = min(dist[i][j - 1] + 1,
                         dist[i - 1][j] + 1,
                         dist[i - 1][j - 1] + (1 if A[i - 1] != B[j - 1] else 0))
    return dist[-1][-1]


if __name__ == '__main__':
    print(solve(*read_input()))
