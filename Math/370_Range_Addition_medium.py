# 这道题和1109是几乎一摸一样的，看1109就行了 不用看这道题了
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        values=[0]*length
        for u in updates:
            values[u[0]]+=u[2]
            if u[1]+1<len(values):
                values[u[1]+1]-=u[2]
        for i in range(1,len(values)):
            values[i]+=values[i-1]
        return values