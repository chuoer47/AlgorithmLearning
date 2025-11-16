class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        st = []
        for x in s:
            if st and st[-1] != x:
                st.pop()
                continue
            st.append(x)
        return len(st)

# class Solution:
#     def minLengthAfterRemovals(self, s: str) -> int:
#         cnt = Counter(s)
#         return abs(cnt["a"] - cnt["b"])