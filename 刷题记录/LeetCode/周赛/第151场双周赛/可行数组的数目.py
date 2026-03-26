class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        left,right = bounds[0]
        ans = right - left + 1
        n = len(original)
        for i in range(n-1):
            d = original[i+1] - original[i]
            nleft,nright = left+d,right+d
            left,right = max(bounds[i+1][0],nleft),min(bounds[i+1][1],nright)
            ans = min(ans,right - left + 1)

            if ans < 0:
                return 0
        return ans