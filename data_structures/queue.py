# 큐
# Silver IV
# https://www.acmicpc.net/problem/10845
from sys import stdin
from collections import deque


def params():
    N = int(stdin.readline())
    instructions = [stdin.readline().split()
                    for _ in range(N)]
    return N, instructions


def solution(N: int, instructions: list[list[str]]):
    queue = deque()
    log = []

    def push(x: int):
        queue.append(x)

    def pop() -> int:
        return queue.popleft() if queue else -1

    def size() -> int:
        return len(queue)

    def empty() -> int:
        return int(not queue)

    def front() -> int:
        return queue[0] if queue else -1

    def back() -> int:
        return queue[-1] if queue else -1

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
        if instruction[0] == 'front':
            log.append(front())
        if instruction[0] == 'back':
            log.append(back())
    return '\n'.join(map(str, log))


if __name__ == '__main__':
    print(solution(*params()))
