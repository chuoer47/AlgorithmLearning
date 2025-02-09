import sys
from collections import Counter
from collections import deque


class AcTrieNode:
    def __init__(self, fa):
        self.s = ''  # end节点自己本身的单词
        self.fail_s = []  # fail指针指向的节点序列的单词列表(如果fail指针指向的节点是一个end节点，此字段保存所有这些单词的列表)
        self.next = {}  # 边和子节点映射
        self.is_end = False  # 是否是end节点
        self.fail = None  # ac自动机的fail指针
        self.fa = fa  # 父节点指针


class AcTrie:
    def __init__(self):
        self.root = AcTrieNode(None)

    def append(self, s: str):
        cur = self.root
        for ch in s:
            if ch not in cur.next:
                new_node = AcTrieNode(cur)
                new_node.s = cur.s + ch
                cur.next[ch] = new_node

            cur = cur.next[ch]
        cur.is_end = True

    # 构建ac自动机接口
    def build(self, s_list):
        # 第一步是构建普通的Trie
        for s in s_list:
            self.append(s)

        # 层次遍历构建Fail指针
        que = deque()
        que.append(self.root)

        depth = 0
        while len(que) > 0:
            node_num = len(que)

            for _ in range(node_num):
                cur = que.popleft()
                if depth == 1:
                    # 根节点下面的第一层word长度是1，是没有后缀的，fail指针全部指向root
                    cur.fail = self.root
                elif depth != 0:
                    cur.fail = self.root

                    # 循环找最长后缀的候选
                    p = cur.fa.fail
                    last_ch = cur.s[-1]
                    while True:
                        if not p:
                            break

                        if last_ch in p.next:
                            cur.fail = p.next[last_ch]

                            f = cur.fail
                            if f.is_end:
                                # 如果fail指针指向的节点是一个end节点，或者这个节点的fail_s列表不为空，需要添加这些单词到cur节点的fail_s列表中
                                cur.fail_s.append(f.s)

                            # fail指针指向的节点中fail_s里面的单词必须全部继承下来，因为这些单词也是后缀的备选
                            for s in f.fail_s:
                                cur.fail_s.append(s)

                            break
                        else:
                            p = p.fail

                for new_node in cur.next.values():
                    que.append(new_node)

            depth += 1

    # 匹配接口, 输出所有匹配的模式串和模式串在T串中的起始位置列表
    def match(self, T, c: Counter):
        words = set()

        cur = self.root
        ans = 0

        idx = 0
        while idx < len(T):
            ch = T[idx]

            if ch in cur.next:
                cur = cur.next[ch]

                if cur.is_end:
                    if cur.s not in words:
                        words.add(cur.s)
                        ans += c[cur.s]

                if len(cur.fail_s) > 0:
                    for s in cur.fail_s:
                        if s not in words:
                            words.add(s)
                            ans += c[s]

                idx += 1
            else:
                if cur.fail:
                    cur = cur.fail
                else:
                    # 当前在root节点，已经没有fail了，那idx位置结尾的子串就找不到任何一个模式串来匹配
                    idx += 1

        return ans

    def getRoot(self) -> AcTrieNode:
        return self.root

    def dfs(self, root, ans):
        if root.is_end:
            ans.append(root.s)

        for next_node in root.next.values():
            self.dfs(next_node, ans)

    # 返回所有符合前缀的字符串
    def getAllPrefixWords(self, prefix, ans):
        root = self.root
        for ch in prefix:
            if ch not in root.next:
                return ans

            root = root.next[ch]

        self.dfs(root, ans)
        return ans

    # 返回是否有match的单词
    def isMatch(self, word) -> bool:
        root = self.root
        for ch in word:
            if ch not in root.next:
                return False

            root = root.next[ch]
        return root.is_end

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())

        words = []
        c = Counter()
        for i in range(n):
            s = sys.stdin.readline().strip()
            words.append(s)
            c[s] += 1

        ac_trie = AcTrie()
        ac_trie.build(words)
        s = sys.stdin.readline().strip()
        ans = ac_trie.match(s, c)

        print(ans)

