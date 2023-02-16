# 트리 순회
# Silver I
# https://www.acmicpc.net/problem/1991
from sys import stdin


def read_input():
    N = int(stdin.readline())
    nodes = {}

    for _ in range(N):
        name, left_child, right_child = map(str, stdin.readline().split())
        nodes[name] = (left_child, right_child)
    return N, nodes


def solve(N: int, tree: dict[str, tuple[str, str]]):
    def preorder():
        log = []

        def search(name: str):
            if name == '.':
                return
            left_child, right_child = tree[name]
            log.append(name)
            search(left_child)
            search(right_child)

        # BEGIN
        search('A')
        return log

    def inorder():
        log = []

        def search(name: str):
            if name == '.':
                return
            left_child, right_child = tree[name]
            search(left_child)
            log.append(name)
            search(right_child)

        # BEGIN
        search('A')
        return log

    def postorder():
        log = []

        def search(name: str):
            if name == '.':
                return
            left_child, right_child = tree[name]
            search(left_child)
            search(right_child)
            log.append(name)

        # BEGIN
        search('A')
        return log

    # BEGIN
    return preorder(), inorder(), postorder()


def print_output(preorder_log: list[str], inorder_log: list[str], postorder_log: list[str]):
    print('\n'.join(''.join(map(str, log))
                    for log in (preorder_log, inorder_log, postorder_log)))


if __name__ == '__main__':
    print_output(*solve(*read_input()))
