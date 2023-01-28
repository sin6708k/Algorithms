# 문자열 반복
# Bronze II
# https://www.acmicpc.net/problem/2675
from sys import stdin


def params():
    T = int(stdin.readline())
    test_cases = [stdin.readline().split()
                  for _ in range(T)]
    return T, test_cases


def solution(T: int, test_cases: list[tuple[int, str]]):
    return '\n'.join(''.join(char * int(repeat)
                             for char in string)
                     for repeat, string in test_cases)


if __name__ == '__main__':
    print(solution(*params()))
