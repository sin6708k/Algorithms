# 트리 순회
# Silver I
# https://www.acmicpc.net/problem/1991
from sys import stdin


def params():
    N = int(stdin.readline())
    nodes = {}

    for _ in range(N):
        name, left_child, right_child = map(str, stdin.readline().split())
        nodes[name] = (left_child, right_child)
    return N, nodes


def solution(N: int, tree: dict[str, tuple[str, str]]):
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
        return ''.join(map(str, log))

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
        return ''.join(map(str, log))

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
        return ''.join(map(str, log))

    # BEGIN
    return '\n'.join([preorder(), inorder(), postorder()])


if __name__ == '__main__':
    print(solution(*params()))
