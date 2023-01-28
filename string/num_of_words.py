# 단어의 개수
# Bronze II
# https://www.acmicpc.net/problem/1152
from sys import stdin


def solution(words: list[str]):
    return len(words)


if __name__ == '__main__':
    print(solution(words=stdin.readline().split()))
