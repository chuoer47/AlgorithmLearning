from collections import defaultdict
from typing import List


class Node:
    def __init__(self):
        self.dic = defaultdict(Node)
        self.delete = False
        self.s = '#'
        self.end = False


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node()
        for path in paths:
            node = root
            for x in path:
                node = node.dic[x]
                node.s = x
            node.end = True
        mapper = defaultdict(int)

        def get_hash(node: Node) -> str:
            if not node.dic:
                return node.s
            childs_hash = sorted([get_hash(child) for child in node.dic.values()])
            childs_hash = "".join(childs_hash)
            mapper[childs_hash] += 1
            node_hash = node.s + "(" + childs_hash + ")"
            return node_hash

        def is_delete(node: Node) -> str:
            if not node.dic:
                return node.s
            childs_hash = sorted([is_delete(child) for child in node.dic.values()])
            childs_hash = "".join(childs_hash)
            if mapper[childs_hash] >= 2:
                node.delete = True
            node_hash = node.s + "(" + childs_hash + ")"
            return node_hash

        get_hash(root)
        is_delete(root)
        print(mapper)
        now = []
        ans = []

        def get_ans(node: Node):
            if node.delete:
                return
            if node.end:
                ans.append(now.copy())
            for nxt in node.dic:
                now.append(nxt)
                get_ans(node.dic[nxt])
                now.pop()

        get_ans(root)
        return ans[1:]
