# �����Ŀ���Ҷ��� �ѵ���Ҫ����ôдcheck����
# ������ʱ��û�������
# ֻ��Ҫ̰�� ������ʱ ����������
# ����ʱ���¼һ�º���һ�� ��ǰ��һ����������ʱ �Ѿ��е����ּ���

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def check(target):
            n = len(points)
            rem = m
            pre = 0
            for i, p in enumerate(points):
                k = (target - 1) // p + 1 - pre
                if i == n - 1 and k <= 0:
                    break
                # ����������һ�����֣�������ζ�Ҫ�����������ߣ�k����Ϊ1
                k = 1 if k < 1 else k
                rem -= k * 2 - 1
                if rem < 0:
                    return False
                pre = k - 1
            return True

        ans = 0
        n = len(points)
        if m < n:
            # ���м���
            return 0
        l, r = 1, min(points) * (m // 2 + 1)
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans
