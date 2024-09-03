"""
https://leetcode.cn/problems/substring-with-concatenation-of-all-words/submissions/561060847/?envType=study-plan-v2&envId=top-interview-150
一开始先暴力破解，发现时间会大量浪费在重复计算
核心思想就是使用滑动窗口减少切割单词的时间
"""

from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        ns = len(s)
        num_word, len_word = len(words), len(words[0])
        cnt = Counter(words)
        cnt2 = None

        for k in range(len_word):
            if k + num_word * len_word > ns:
                break

            for i in range(k, ns, len_word):
                if (ns - i + 1) // len_word < num_word:  # 剪枝
                    break
                if i == k:  # 第一次，要全部加载进来
                    tem = []
                    for j in range(num_word):
                        tem.append(s[i + j * len_word:i + j * len_word + len_word])
                    cnt2 = Counter(tem)
                else:  # 不是第一次，就只需要出一个，加一个，滑动窗口即可
                    pre = s[i - len_word:i]
                    cnt2[pre] -= 1
                    if cnt2[pre] == 0:
                        del cnt2[pre]
                    now = s[i + (num_word - 1) * len_word:i + num_word * len_word]
                    cnt2[now] += 1
                if cnt == cnt2:
                    ans.append(i)
        return ans
