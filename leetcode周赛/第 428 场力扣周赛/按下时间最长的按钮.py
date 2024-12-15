class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        pre = 0
        cnt = Counter()
        for index,time in events:
            cnt[index] = max(cnt[index],time - pre)
            pre = time
        arr = [(v,k) for k,v in cnt.items()]
        # arr.sort()
        return sorted(arr,key =lambda x:(x[0],-x[1]))[-1][1]