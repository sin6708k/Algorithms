# 상자넣기
# https://www.acmicpc.net/problem/1965
from sys import stdin
from itertools import islice


if __name__ == '__main__':
    N = int(stdin.readline())
    boxes = list(map(int, input().split()))
    count_memo = [0] * N

    for i, box_i in enumerate(boxes):
        count_memo[i] = max((count_j + 1
                             for count_j, box_j in zip(islice(count_memo, i), boxes)
                             if box_j < box_i),
                            default=1)

    print(max(count_memo))
