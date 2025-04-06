from collections import defaultdict
from typing import List


class Node:
    def __init__(self):
        self.dic: defaultdict[str] = defaultdict(Node)
        self.tail = False
        self.target = {-1}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, idx):
        n = len(word)
        now = self.root

        for i in range(n):
            if word[i] not in now.dic:
                now.dic[word[i]] = Node()
            now = now.dic[word[i]]
            now.target.add(idx)
        now.tail = True

    def search(self, word):
        n = len(word)
        now = self.root
        for i in range(n):
            now = now.dic[word[i]]
        return now.target


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pre = Trie()
        suff = Trie()
        for i, word in enumerate(words):
            pre.insert(word, i)
            suff.insert(word[::-1], i)
        ans = 0
        for i, word in enumerate(words):
            pre_set = pre.search(word)
            suff_set = suff.search(word[::-1])
            ans += len(pre_set & suff_set) - 1
        return ans
