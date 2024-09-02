from typing import List


class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        # write code here
        num.sort()  # 排序
        n = len(num)
        ans = set()
        dic = [[] for _ in range(0, 400010)]  # 这里需要对应修改
        for i in range(n):
            for j in range(i + 1, n):
                dic[num[i] + num[j]].append((i, j))

        for i in range(n):
            for x, y in dic[-num[i]]:
                if i == x or i == y:
                    continue
                else:
                    tem = [num[i], num[x], num[y]]
                    tem.sort()
                    ans.add((tem[0], tem[1], tem[2]))
        ans = [list(i) for i in ans]
        ans.sort()
        return ans


if __name__ == '__main__':
    s = Solution()
    num = [0, 1, -5, -4, 0, -4, 1]
    print(s.threeSum(num))
