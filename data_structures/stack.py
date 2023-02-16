# 스택
# Silver IV
# https://www.acmicpc.net/problem/10828
from sys import stdin


def read_input():
    N = int(stdin.readline())
    instructions = [stdin.readline().split()
                    for _ in range(N)]
    return N, instructions


def solve(N: int, instructions: list[list[str]]):
    stack = []
    log = []

    def push(x: int):
        stack.append(x)

    def pop() -> int:
        return stack.pop() if stack else -1

    def size() -> int:
        return len(stack)

    def empty() -> int:
        return int(not stack)

    def top() -> int:
        return stack[-1] if stack else -1

    # BEGIN
    for instruction in instructions:
        if instruction[0] == 'push':
            push(int(instruction[1]))
        if instruction[0] == 'pop':
            log.append(pop())
        if instruction[0] == 'size':
            log.append(size())
        if instruction[0] == 'empty':
            log.append(empty())
        if instruction[0] == 'top':
            log.append(top())
    return log


def print_output(log: list[int]):
    print('\n'.join(map(str, log)))


if __name__ == '__main__':
    print_output(solve(*read_input()))
