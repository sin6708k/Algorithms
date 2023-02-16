# 단어의 개수
# Bronze II
# https://www.acmicpc.net/problem/1152
from sys import stdin


def read_input():
    return stdin.readline()


def solve(string: str):
    return len(string.split())


if __name__ == '__main__':
    print(solve(read_input()))
