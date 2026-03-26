class Solution:
    def countPairs(self, words: List[str]) -> int:
        # 前缀和，保存开头为a的情况的哈希表就好
        # 然后遍历，时间复杂度
        cnt = defaultdict(int)
        ans = 0
        for i,v in enumerate(words):
            v = [ord(i) - ord('a') for i in v]
            move = v[0]
            v = [ (i - move) % 26 for i in v]
            v = "".join(chr(ord('a') + i) for i in v)
            ans += cnt[v]
            cnt[v] += 1
        return ans
    