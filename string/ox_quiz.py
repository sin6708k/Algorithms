# OX퀴즈
# https://www.acmicpc.net/problem/8958
from sys import stdin


if __name__ == '__main__':
    test_cases = stdin.readlines()

    for test_case in test_cases:
        a, b = map(int, test_case.split())
        print(a + b)
