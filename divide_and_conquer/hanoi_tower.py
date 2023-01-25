# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729
from sys import stdin


def move(index: int, origin: int, waypoint: int, dest: int):
    global log

    if index == 0:
        return

    move(index - 1, origin, dest, waypoint)
    log.append('%d %d' % (origin, dest))
    move(index - 1, waypoint, origin, dest)


if __name__ == '__main__':
    N = int(stdin.readline())
    log = []

    move(N, 1, 2, 3)
    print(len(log))
    print('\n'.join(log))
