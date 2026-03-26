# coding=gb2312
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        record = [[0] * i for i in range(10)]
        for i in range(n):
            c = int(s[i])
            # 先进行转移
            tmp = [[0] * i for i in range(10)]
            for i in range(1, 10):
                tmp[i][c % i] += 1
            # 下面对每个mod进行转移
            for i in range(1, 10):
                for j in range(i):
                    tmp[i][(j * 10 + c) % i] += record[i][j]

            record = tmp
            if c > 0:
                ans += record[c][0]

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings(s="5701283"))
