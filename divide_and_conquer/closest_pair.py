# 가장 가까운 두 점
# https://www.acmicpc.net/problem/2261
from sys import stdin
from itertools import islice


def dist(v: tuple, u: tuple) -> int:
    return (v[0] - u[0]) ** 2 + (v[1] - u[1]) ** 2


def search_closest_dist(vertices: list[tuple[int, int]]) -> int:
    n = len(vertices)

    if n < 2:
        return W
    if n == 2:
        v, u = vertices
        return dist(v, u)
    if n == 3:
        v, u, k = vertices
        return min(dist(v, u), dist(v, k), dist(u, k))

    mid = n // 2
    left_vertices = vertices[:mid]
    right_vertices = vertices[mid:]
    closest_dist = min(search_closest_dist(left_vertices),
                       search_closest_dist(right_vertices))

    m = vertices[mid]
    center_vertices = []
    for v in reversed(left_vertices):
        if closest_dist <= (v[0] - m[0]) ** 2:
            break
        center_vertices.append(v)
    for v in right_vertices:
        if closest_dist <= (v[0] - m[0]) ** 2:
            break
        center_vertices.append(v)
    center_vertices.sort(key=lambda x: x[1])

    for i, v in enumerate(center_vertices):
        for u in islice(center_vertices, i + 1, i + 7):
            if closest_dist <= (u[1] - v[1]) ** 2:
                break
            closest_dist = min(closest_dist, dist(v, u))
    return closest_dist


if __name__ == '__main__':
    N = int(stdin.readline())
    W = dist((-10000, -10000), (10000, 10000)) + 1
    vertices = sorted([tuple(map(int, stdin.readline().split()))
                       for _ in range(N)])

    print(search_closest_dist(vertices))
