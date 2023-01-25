# 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197
from sys import stdin
from heapq import heapify, heappop


class DisjointSet:
    def __init__(self, n):
        self.__roots = list(range(n))

    def find(self, v: int) -> int:
        if self.__roots[v] != v:
            self.__roots[v] = self.find(self.__roots[v])
        return self.__roots[v]

    def union(self, v: int, u: int):
        root_of_v = self.find(v)
        root_of_u = self.find(u)
        if root_of_v < root_of_u:
            self.__roots[root_of_v] = root_of_u
        else:
            self.__roots[root_of_u] = root_of_v


if __name__ == '__main__':
    V, E = map(int, stdin.readline().split())
    edges = [(w, v, u)
             for v, u, w in (map(int, stdin.readline().split())
                             for _ in range(E))]
    heapify(edges)
    connected = DisjointSet(V + 1)
    sum_weight = 0

    while edges:
        w, v, u = heappop(edges)
        root_of_v = connected.find(v)
        root_of_u = connected.find(u)
        if root_of_v != root_of_u:
            connected.union(root_of_v, root_of_u)
            sum_weight += w

    print(sum_weight)
