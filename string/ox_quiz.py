# OX퀴즈
# Bronze II
# https://www.acmicpc.net/problem/8958
from sys import stdin


def read_input():
    T = int(stdin.readline())
    test_cases = [stdin.readline().rstrip()
                  for _ in range(T)]
    return T, test_cases


def solve(T: int, test_cases: list[str]):
    def accumulate_score(test_case: str):
        count = 0
        score = 0

        for char in test_case:
            if char == 'O':
                count += 1
                score += count
            else:
                count = 0
        return score

    # BEGIN
    return list(map(accumulate_score, test_cases))


def print_output(scores: list[int]):
    print('\n'.join(map(str, scores)))


if __name__ == '__main__':
    print_output(solve(*read_input()))
