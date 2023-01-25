# 단어 공부
# https://www.acmicpc.net/problem/1157
from sys import stdin
from collections import Counter


if __name__ == '__main__':
    word = stdin.readline().rstrip().upper()
    counter = Counter(word).most_common()
    n = len(counter)

    if n >= 2:
        most_common_char, max_count = counter[0]
        _, second_count = counter[1]

        if max_count != second_count:
            print(most_common_char)
        else:
            print('?')
    elif n == 1:
        most_common_char, max_count = counter[0]
        print(most_common_char)
    else:
        print('?')
