# 덱
# Silver IV
# https://www.acmicpc.net/problem/10866
from sys import stdin
from collections import deque


def params():
    N = int(stdin.readline())
    instructions = [stdin.readline().split()
                    for _ in range(N)]
    return N, instructions


def solution(N: int, instructions: list[list[str]]):
    dequeue = deque()
    log = []

    def push_front(x: int):
        dequeue.appendleft(x)

    def push_back(x: int):
        dequeue.append(x)

    def pop_front() -> int:
        return dequeue.popleft() if dequeue else -1

    def pop_back() -> int:
        return dequeue.pop() if dequeue else -1

    def size() -> int:
        return len(dequeue)

    def empty() -> int:
        return int(not dequeue)

    def front() -> int:
        return dequeue[0] if dequeue else -1

    def back() -> int:
        return dequeue[-1] if dequeue else -1

    # BEGIN
    for instruction in instructions:
        if instruction[0] == 'push_front':
            push_front(int(instruction[1]))
        if instruction[0] == 'push_back':
            push_back(int(instruction[1]))
        if instruction[0] == 'pop_front':
            log.append(pop_front())
        if instruction[0] == 'pop_back':
            log.append(pop_back())
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

