# 괄호
# Silver IV
# https://www.acmicpc.net/problem/9012
from sys import stdin


def read_input():
    T = int(stdin.readline())
    strings = [stdin.readline().rstrip()
               for _ in range(T)]
    return T, strings


def solve(N: int, strings: list[str]):
    def valid(string: str) -> bool:
        stack = []
        for char in string:
            if char == '(':
                stack.append(char)
            if char == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        return False if stack else True

    # BEGIN
    return list(map(valid, strings))


def print_output(strings_valid: list[bool]):
    print('\n'.join('YES' if string_valid else 'NO'
                    for string_valid in strings_valid))


if __name__ == '__main__':
    print_output(solve(*read_input()))
