# 직각삼각형
# Bronze III
# https://www.acmicpc.net/problem/4153
from sys import stdin


def param():
    triangles = []
    while True:
        sides = sorted(map(int, stdin.readline().split()))
        if sides == [0, 0, 0]:
            break
        triangles.append(sides)
    return triangles


def solution(triangles: list[list[int]]):
    def right(triangle: list[int]) -> bool:
        return triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2

    # BEGIN
    return '\n'.join('right' if right(triangle) else 'wrong'
                     for triangle in triangles)


if __name__ == '__main__':
    print(solution(param()))
