# 최대 힙
# Silver II
# https://www.acmicpc.net/problem/11279
from sys import stdin
from heapq import heappush, heappop


def read_input():
    N = int(stdin.readline())
    operations = [int(stdin.readline())
                  for _ in range(N)]
    return N, operations


def solve(N: int, operations: list[int]):
    heap = []
    log = []
    for operation in operations:
        if operation != 0:
            heappush(heap, -operation)
        else:
            log.append(-heappop(heap) if heap else 0)
    return log


def print_output(log: list[int]):
    print('\n'.join(map(str, log)))


if __name__ == '__main__':
    print_output(solve(*read_input()))
