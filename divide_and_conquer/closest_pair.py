# 가장 가까운 두 점
# Platinum II
# https://www.acmicpc.net/problem/2261
from sys import stdin
from itertools import islice


def read_input():
    N = int(stdin.readline())
    all_vertices = sorted([tuple(map(int, stdin.readline().split()))
                           for _ in range(N)])
    return N, all_vertices


def dist(v: tuple, u: tuple) -> int:
    return (v[0] - u[0]) ** 2 + (v[1] - u[1]) ** 2


def solve(N: int, all_vertices: list[tuple[int, ...]]):
    def find_closest_dist(vertices: list[tuple[int, ...]]) -> int:
        if len(vertices) < 2:
            return 10 ** 9
        if len(vertices) == 2:
            return dist(vertices[0], vertices[1])
        if len(vertices) == 3:
            return min(dist(vertices[0], vertices[1]),
                       dist(vertices[0], vertices[2]),
                       dist(vertices[1], vertices[2]))

        mid = len(vertices) // 2
        left_vertices = vertices[:mid]
        right_vertices = vertices[mid:]
        closest_dist = min(find_closest_dist(left_vertices),
                           find_closest_dist(right_vertices))

        center_vertices = []
        for v in reversed(left_vertices):
            if closest_dist <= (v[0] - vertices[mid][0]) ** 2:
                break
            center_vertices.append(v)
        for v in right_vertices:
            if closest_dist <= (v[0] - vertices[mid][0]) ** 2:
                break
            center_vertices.append(v)
        center_vertices.sort(key=lambda x: x[1])

        for i, v in enumerate(center_vertices):
            for u in islice(center_vertices, i + 1, i + 7):
                if closest_dist <= (u[1] - v[1]) ** 2:
                    break
                closest_dist = min(closest_dist, dist(v, u))
        return closest_dist

    # BEGIN
    return find_closest_dist(all_vertices)


if __name__ == '__main__':
    print(solve(*read_input()))
