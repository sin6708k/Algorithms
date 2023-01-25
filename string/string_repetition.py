# 문자열 반복
# https://www.acmicpc.net/problem/2675
from sys import stdin


if __name__ == '__main__':
    T = int(stdin.readline())
    test_cases = [stdin.readline().split()
                  for _ in range(T)]

    for repeat, string in test_cases:
        print(''.join((char * int(repeat)
                       for char in string)))
