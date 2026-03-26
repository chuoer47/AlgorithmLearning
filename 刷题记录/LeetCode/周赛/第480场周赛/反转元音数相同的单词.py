class Solution:
    def reverseWords(self, s: str) -> str:
        def count(s):
            vowels = "aeiou"
            return sum(int(i in vowels) for i in s)

        s = list(s.split())
        p = count(s[0])
        for i in range(1, len(s)):
            if count(s[i]) == p:
                s[i] = s[i][::-1]
        return " ".join(s)
