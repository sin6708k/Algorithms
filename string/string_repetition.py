# 문자열 반복
# Bronze II
# https://www.acmicpc.net/problem/2675
from sys import stdin


def test_case_tuple(split: list[str]) -> tuple[int, str]:
    return int(split[0]), split[1]


def read_input():
    T = int(stdin.readline())
    test_cases = [test_case_tuple(stdin.readline().split())
                  for _ in range(T)]
    return T, test_cases


def solve(T: int, test_cases: list[tuple[int, str]]):
    return [[char * repeat
             for char in string]
            for repeat, string in test_cases]


def print_output(strings: list[list[str]]):
    print('\n'.join(''.join(string)
                    for string in strings))


if __name__ == '__main__':
    print_output(solve(*read_input()))
