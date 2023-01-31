# 괄호
# Silver IV
# https://www.acmicpc.net/problem/9012
from sys import stdin


def params():
    T = int(stdin.readline())
    strings = [stdin.readline().rstrip()
               for _ in range(T)]
    return T, strings


def solution(N: int, strings: list[str]):
    def valid(string: str) -> bool:
        stack = []
        for char in string:
            if char == '(':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return False if stack else True

    # BEGIN
    return '\n'.join('YES' if valid(string) else 'NO'
                     for string in strings)


if __name__ == '__main__':
    print(solution(*params()))
