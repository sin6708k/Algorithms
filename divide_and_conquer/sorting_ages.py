# 나이순 정렬
# Silver V
# https://www.acmicpc.net/problem/10814
from sys import stdin


def member_tuple(split: list[str]) -> tuple[int, str]:
    return int(split[0]), split[1]


def params():
    N = int(stdin.readline())
    all_members = [member_tuple(stdin.readline().split())
                   for _ in range(N)]
    return N, all_members


# Implemented by merge sort
def solution(N: int, all_members: list[tuple[int, str]]):
    def merge(left_members: list[tuple[int, str]],
              right_members: list[tuple[int, str]]) -> list[tuple[int, str]]:
        i = 0
        j = 0
        nums = []

        while True:
            if i == len(left_members):
                nums.extend(right_members[j:])
                break
            if j == len(right_members):
                nums.extend(left_members[i:])
                break

            if left_members[i][0] <= right_members[j][0]:
                nums.append(left_members[i])
                i += 1
            else:
                nums.append(right_members[j])
                j += 1
        return nums

    def sort(members: list[tuple[int, str]]) -> list[tuple[int, str]]:
        if len(members) == 1:
            return members

        mid = len(members) // 2
        return merge(sort(members[:mid]), sort(members[mid:]))

    # BEGIN
    return '\n'.join(' '.join(map(str, member))
                     for member in sort(all_members))


if __name__ == '__main__':
    print(solution(*params()))
