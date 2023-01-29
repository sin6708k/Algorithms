# 2-SAT - 1
# Silver I
# https://www.acmicpc.net/problem/11277
from sys import stdin
from itertools import product


def params():
    N, M = map(int, stdin.readline().split())
    clauses = [tuple(map(int, stdin.readline().split()))
               for _ in range(M)]
    return N, M, clauses


def solution(N: int, M: int, clauses: list[tuple[int, int]]):

    return int(any(all(any((term > 0) == variables[abs(term) - 1]
                           for term in clause)
                       for clause in clauses)
                   for variables in product([False, True], repeat=N)))


if __name__ == '__main__':
    print(solution(*params()))
