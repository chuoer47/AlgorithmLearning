from typing import List

# 纯模拟
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        online = [1] * numberOfUsers
        offlinetime = [-1] * numberOfUsers
        events = [[i, int(j), k] for i, j, k in events]
        events.sort(key=lambda x: (x[1], -ord(x[0][0])))
        for event, time, msg in events:
            # 让下线的上线
            for i in range(numberOfUsers):
                if online[i] == 0 and time - offlinetime[i] >= 60:
                    online[i] = 1
            # 分别处理消息
            if event == "MESSAGE":
                if msg[0] == "A":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif msg[0] == "i":
                    for user in msg.split(" "):
                        userid = int(user[2:])
                        mentions[userid] += 1
                elif msg[0] == "H":
                    for i in range(numberOfUsers):
                        if online[i] == 1:
                            mentions[i] += 1
            elif event == "OFFLINE":
                userid = int(msg)
                offlinetime[userid] = time
                online[userid] = 0
        return mentions


if __name__ == '__main__':
    s = Solution()
    print(s.countMentions(numberOfUsers=3,
                          events=[["MESSAGE", "5", "HERE"], ["OFFLINE", "10", "0"], ["MESSAGE", "15", "HERE"],
                                  ["OFFLINE", "18", "2"], ["MESSAGE", "20", "HERE"]]))
