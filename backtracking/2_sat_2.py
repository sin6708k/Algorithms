# 2-SAT - 2
# Silver I
# https://www.acmicpc.net/problem/11278
from sys import stdin
from itertools import product


def params():
    N, M = map(int, stdin.readline().split())
    clauses = [tuple(map(int, stdin.readline().split()))
               for _ in range(M)]
    return N, M, clauses


def solution(N: int, M: int, clauses: list[tuple[int, int]]):

    for variables in product([False, True], repeat=N):
        if all(any((term > 0) == variables[abs(term) - 1]
                   for term in clause)
               for clause in clauses):
            return '1\n' + ' '.join(map(str, map(int, variables)))
    return 0


if __name__ == '__main__':
    print(solution(*params()))
