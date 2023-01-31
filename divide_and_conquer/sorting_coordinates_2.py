# 좌표 정렬하기 2
# Silver V
# https://www.acmicpc.net/problem/11651
from sys import stdin


def params():
    N = int(stdin.readline())
    all_coordinates = [tuple(map(int, stdin.readline().split()))
                       for _ in range(N)]
    return N, all_coordinates


# Implemented by merge sort
def solution(N: int, all_coordinates: list[tuple[int, int]]):
    def merge(left_coordinates: list[tuple[int, int]],
              right_coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
        i = 0
        j = 0
        nums = []

        while True:
            if i == len(left_coordinates):
                nums.extend(right_coordinates[j:])
                break
            if j == len(right_coordinates):
                nums.extend(left_coordinates[i:])
                break

            if tuple(reversed(left_coordinates[i])) <= tuple(reversed(right_coordinates[j])):
                nums.append(left_coordinates[i])
                i += 1
            else:
                nums.append(right_coordinates[j])
                j += 1
        return nums

    def sort(coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
        if len(coordinates) == 1:
            return coordinates

        mid = len(coordinates) // 2
        return merge(sort(coordinates[:mid]), sort(coordinates[mid:]))

    # BEGIN
    return '\n'.join(' '.join(map(str, coordinate))
                     for coordinate in sort(all_coordinates))


if __name__ == '__main__':
    print(solution(*params()))
