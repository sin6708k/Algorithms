# 최소 편집
# https://www.acmicpc.net/problem/15483
from sys import stdin


if __name__ == '__main__':
    A = stdin.readline()
    B = stdin.readline()
    N = len(A)
    M = len(B)
    dist_memo = [[i if j == 0 else
                  j if i == 0 else
                  0 for j in range(M + 1)]
                 for i in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dist_memo[i][j] = min(dist_memo[i][j - 1] + 1,
                                  dist_memo[i - 1][j] + 1,
                                  dist_memo[i - 1][j - 1] + (1 if A[i - 1] != B[j - 1] else 0))

    print(dist_memo[N][M])
