class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # 直接暴力打满得了
        nums = []
        for x in product(words,repeat=4):
            top,left,right,bottom = x
            if len(set(x)) == 4:
                if top[0] == left[0] and top[3] == right[0] and bottom[0] == left[3] and bottom[3] == right[3]:
                    nums.append(list(x))
        return sorted(nums)