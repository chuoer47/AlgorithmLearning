"""
https://leetcode.cn/problems/sliding-window-maximum/description/
一维滑动窗口
"""
from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """
    第一种写法，初始化代码较为冗余的
    :param nums:
    :param k:
    :return:
    """
    q = deque()  # 维系下标
    res = []  # 存储结果的数组
    tt = []
    # 初始化前k个窗口
    for i in range(k):
        tt.append([nums[i], i])
    tt.sort(reverse=True)
    for i in range(k):
        q.append(tt[i][1])
    # 加入第一个答案
    res.append(nums[q[0]])
    # 下面开始滑动
    l, r = 1, k
    while r < len(nums):
        rv = nums[r]
        # 保持单调队列
        while q and nums[q[-1]] < rv:
            q.pop()
        q.append(r)
        # 把不符合条件的剔除出去
        while not l <= q[0] <= r:
            q.popleft()
        res.append(nums[q[0]])
        l += 1
        r += 1
    return res


def maxSlidingWindow2(nums: List[int], k: int) -> List[int]:
    """
    第二种写法，改变初始化方法
    :param nums:
    :param k:
    :return:
    """
    q = deque()  # 维系下标
    res = []  # 存储结果的数组
    # 初始化前k个窗口
    for i in range(k):
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)
    # 加入第一个答案
    res.append(nums[q[0]])
    # 下面开始滑动
    l, r = 1, k
    while r < len(nums):
        rv = nums[r]
        # 保持单调队列
        while q and nums[q[-1]] < rv:
            q.pop()
        q.append(r)
        # 把不符合条件的剔除出去
        while not l <= q[0] <= r:
            q.popleft()
        res.append(nums[q[0]])
        l += 1
        r += 1
    return res


if __name__ == '__main__':
    nums = [9, 10, 9, -7, -4, -8, 2, -6]
    k = 5
    s = maxSlidingWindow2(nums, k)
    print(s)
