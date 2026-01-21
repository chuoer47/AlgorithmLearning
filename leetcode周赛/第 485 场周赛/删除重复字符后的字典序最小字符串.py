class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        cnt = Counter(s)
        st = []
        for x in s:
            while st and st[-1] > x and cnt[st[-1]] >= 2:
                cnt[st.pop()] -= 1
            st.append(x)
        while cnt[st[-1]] > 1:
            cnt[st.pop()] -= 1
        return "".join(st)