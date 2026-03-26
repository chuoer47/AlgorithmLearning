class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        st = []
        for x in s:
            if x in st[-k:]:
                continue
            st.append(x)
        return "".join(st)