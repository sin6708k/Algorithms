# 회의실 배정
# https://www.acmicpc.net/problem/1931
from sys import stdin
from heapq import heapify, heappop


if __name__ == '__main__':
    N = int(stdin.readline())
    meetings = [(end, start)
                for start, end in (tuple(map(int, stdin.readline().split()))
                                   for _ in range(N))]
    heapify(meetings)
    last = 0
    count = 0

    while meetings:
        end, start = heappop(meetings)
        if last <= start:
            last = end
            count += 1

    print(count)
