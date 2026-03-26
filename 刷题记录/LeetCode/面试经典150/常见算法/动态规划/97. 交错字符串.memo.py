class Solution:
    dic = {}

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check if the lengths match
        if len(s3) != len(s1) + len(s2):
            return False

        # Use pointers to track positions in s1, s2, and s3
        left, right, now = 0, 0, 0

        while left < len(s1) and right < len(s2) and now < len(s3):
            # Check for matches and explore both options
            if s1[left] == s3[now] and s2[right] == s3[now]:
                # Try advancing either string
                if self.tryInterleave(s1[left + 1:], s2[right:], s3[now + 1:]) or \
                        self.tryInterleave(s1[left:], s2[right + 1:], s3[now + 1:]):
                    return True
                return False

            # Advance the pointer for matching characters
            if s1[left] == s3[now]:
                left += 1
            elif s2[right] == s3[now]:
                right += 1
            else:
                return False

            now += 1

        # Check if the remaining characters in either s1 or s2 match s3
        return s1[left:] == s3[now:] or s2[right:] == s3[now:]

    def tryInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Use memoization to store results
        if (s1, s2, s3) in self.dic:
            return self.dic[(s1, s2, s3)]

        result = self.isInterleave(s1, s2, s3)
        self.dic[(s1, s2, s3)] = result
        return result
