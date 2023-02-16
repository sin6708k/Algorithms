# 2-SAT - 1
# Silver I
# https://www.acmicpc.net/problem/11277
from sys import stdin
from itertools import product


def read_input():
    N, M = map(int, stdin.readline().split())
    clauses = [tuple(map(int, stdin.readline().split()))
               for _ in range(M)]
    return N, M, clauses


def solve(N: int, M: int, clauses: list[tuple[int, int]]):

    return any(all(any((term > 0) == variables[abs(term) - 1]
                       for term in clause)
                   for clause in clauses)
               for variables in product([False, True], repeat=N))


def print_output(f: bool):
    print(int(f))


if __name__ == '__main__':
    print_output(solve(*read_input()))
