# 회의실 배정
# Silver I
# https://www.acmicpc.net/problem/1931
from sys import stdin
from heapq import heapify, heappop


def read_input():
    N = int(stdin.readline())
    meetings = [tuple(reversed(tuple(map(int, stdin.readline().split()))))
                for _ in range(N)]
    heapify(meetings)
    return N, meetings


def solve(N: int, meetings: list[tuple[int, int]]):
    last = 0
    count = 0

    while meetings:
        end, start = heappop(meetings)
        if last <= start:
            last = end
            count += 1
    return count


if __name__ == '__main__':
    print(solve(*read_input()))
