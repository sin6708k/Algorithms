# 최대공약수와 최소공배수
# Bronze I
# https://www.acmicpc.net/problem/2609
from sys import stdin


def read_input():
    A, B = map(int, stdin.readline().split())
    return A, B


def solve(A: int, B: int):
    gcd = 1
    for n in range(2, max(A, B) + 1):
        if A % n == 0 and B % n == 0:
            gcd = n

    lcm = max(A, B)
    while not (lcm % A == 0 and lcm % B == 0):
        lcm += gcd

    return gcd, lcm


def print_output(gcd: int, lcm: int):
    print(gcd)
    print(lcm)


if __name__ == '__main__':
    print_output(*solve(*read_input()))
