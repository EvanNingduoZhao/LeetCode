# 这题非常简单
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxTime=releaseTimes[0]
        maxKey=keysPressed[0]
        for i in range(1,len(releaseTimes)):
            duration = releaseTimes[i]-releaseTimes[i-1]
            if duration>=maxTime:
                if duration == maxTime:
                    maxKey = max(maxKey,keysPressed[i])
                else:
                    maxKey=keysPressed[i]
                    maxTime = duration
        return maxKey