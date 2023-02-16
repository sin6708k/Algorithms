# 단어 공부
# Bronze I
# https://www.acmicpc.net/problem/1157
from sys import stdin
from collections import Counter


def read_input():
    return stdin.readline().rstrip()


def solve(words: str):
    counter = Counter(words.upper()).most_common()

    if len(counter) >= 2:
        most_common_char, count_of_most_common = counter[0]
        _, count_of_second_common = counter[1]

        if count_of_most_common != count_of_second_common:
            return most_common_char
        else:
            return '?'
    elif len(counter) == 1:
        most_common_char, _ = counter[0]
        return most_common_char
    else:
        return '?'


if __name__ == '__main__':
    print(solve(read_input()))
