# 수 정렬하기 3
# Bronze I
# https://www.acmicpc.net/problem/10989
from sys import stdin, stdout


def read_input():
    return int(stdin.readline())


def solve(N: int):
    counter = [0] * 10001

    for _ in range(N):
        i = int(stdin.readline())
        counter[i] += 1

    for i in range(1, 10001):
        for _ in range(counter[i]):
            stdout.write('%d\n' % i)


if __name__ == '__main__':
    solve(read_input())
