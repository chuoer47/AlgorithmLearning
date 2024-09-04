class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        # write code here
        # num.sort()  # 排序
        n = len(num)
        ans = set()
        dic = {}
        for i in range(n):
            for j in range(i + 1, n):
                if num[i] + num[j] in dic:
                    dic[num[i] + num[j]].add((i, j))
                else:
                    dic[num[i] + num[j]] = {(i, j)}

        for i in range(n):
            for x, y in dic.get(-num[i], {}):
                if i == x or i == y:
                    continue
                else:
                    tem = [num[i], num[x], num[y]]
                    tem.sort()
                    ans.add((tem[0], tem[1], tem[2]))
        ans = [list(i) for i in ans]
        return ans
