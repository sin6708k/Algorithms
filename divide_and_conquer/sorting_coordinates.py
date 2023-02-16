# 좌표 정렬하기
# Silver V
# https://www.acmicpc.net/problem/11650
from sys import stdin


def read_input():
    N = int(stdin.readline())
    all_coordinates = [tuple(map(int, stdin.readline().split()))
                       for _ in range(N)]
    return N, all_coordinates


# Implemented by merge sort
def solve(N: int, all_coordinates: list[tuple[int, int]]):
    def merge(left_coordinates: list[tuple[int, int]],
              right_coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
        i = 0
        j = 0
        coordinates = []

        while True:
            if i == len(left_coordinates):
                coordinates.extend(right_coordinates[j:])
                break
            if j == len(right_coordinates):
                coordinates.extend(left_coordinates[i:])
                break

            if left_coordinates[i] <= right_coordinates[j]:
                coordinates.append(left_coordinates[i])
                i += 1
            else:
                coordinates.append(right_coordinates[j])
                j += 1
        return coordinates

    def sort(coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
        if len(coordinates) == 1:
            return coordinates

        mid = len(coordinates) // 2
        return merge(sort(coordinates[:mid]), sort(coordinates[mid:]))

    # BEGIN
    return sort(all_coordinates)


def print_output(coordinates: list[tuple[int, int]]):
    print('\n'.join(' '.join(map(str, coordinate))
                    for coordinate in coordinates))


if __name__ == '__main__':
    print_output(solve(*read_input()))
