# 직각삼각형
# Bronze III
# https://www.acmicpc.net/problem/4153
from sys import stdin


def read_input():
    triangles = []
    while True:
        triangle = tuple(map(int, stdin.readline().split()))
        if triangle == (0, 0, 0):
            break
        triangles.append(triangle)
    return triangles


def solve(triangles: list[tuple[int, ...]]):
    return [triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2
            for triangle in map(sorted, triangles)]


def print_output(triangles_right: list[bool]):
    print('\n'.join('right' if triangle_right else 'wrong'
                    for triangle_right in triangles_right))


if __name__ == '__main__':
    print_output(solve(read_input()))
