# OX퀴즈
# Bronze II
# https://www.acmicpc.net/problem/8958
from sys import stdin


def solution(test_cases: list[str]):
    return '\n'.join(map(str, (sum(map(int, test_case.split()))
                               for test_case in test_cases)))


if __name__ == '__main__':
    print(solution(test_cases=stdin.readlines()))
