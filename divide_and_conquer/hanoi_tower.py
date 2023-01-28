# 하노이 탑 이동 순서
# Silver I
# https://www.acmicpc.net/problem/11729
from sys import stdin
from collections import deque


def solution(N: int) -> str:
    log = deque()

    def move(index: int, origin: int, waypoint: int, dest: int):
        if index == 0:
            return

        move(index - 1, origin, dest, waypoint)
        log.append('%d %d' % (origin, dest))
        move(index - 1, waypoint, origin, dest)

    # BEGIN
    move(N, 1, 2, 3)
    log.appendleft(len(log))
    return '\n'.join(map(str, log))


if __name__ == '__main__':
    print(solution(N=int(stdin.readline())))
