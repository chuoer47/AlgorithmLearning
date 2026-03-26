letter_mapping = {
    'a': 'b',
    'b': 'a',
    'c': 'd',
    'd': 'c',
    'e': 'f',
    'f': 'e',
    'g': 'h',
    'h': 'g',
    'i': 'j',
    'j': 'i',
    'k': 'l',
    'l': 'k',
    'm': 'n',
    'n': 'm',
    'o': 'p',
    'p': 'o',
    'q': 'r',
    'r': 'q',
    's': 't',
    't': 's',
    'u': 'v',
    'v': 'u',
    'w': 'x',
    'x': 'w',
    'y': 'z',
    'z': 'a'
}


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = int(1e9 + 7)
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1
        for i in range(t):
            nxt = [0] * 26
            for k, v in enumerate(cnt):  # 最多26个字母
                c = (k + 1) % 26
                nxt[c] = (nxt[c] + v) % mod
                if c == 0:
                    nxt[1] = (nxt[1] + v) % mod
            cnt = nxt
        ans = sum(cnt) % mod
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthAfterTransformations(s="abcyy", t=2))
