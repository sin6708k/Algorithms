# 상자넣기
# https://www.acmicpc.net/problem/1965
from sys import stdin
from itertools import islice


if __name__ == '__main__':
    N = int(stdin.readline())
    boxes = list(map(int, stdin.readline().split()))
    count_memo = [0] * N

    for i in range(N):
        count_memo[i] = max((count_memo[j] + 1
                             for j in range(i)
                             if boxes[j] < boxes[i]),
                            default=1)

    print(max(count_memo))
