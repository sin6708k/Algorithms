# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729
from sys import stdin


def move(index: int, origin: int, waypoint: int, dest: int):
    global recode

    if index == 0:
        return

    move(index - 1, origin, dest, waypoint)
    recode.append('%d %d' % (origin, dest))
    move(index - 1, waypoint, origin, dest)


if __name__ == '__main__':
    N = int(stdin.readline())
    recode = []

    move(N, 1, 2, 3)
    print(len(recode))
    print('\n'.join(recode))
