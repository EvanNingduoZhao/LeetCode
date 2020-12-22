class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rCount=0
        lCount=0
        splittedCount=0
        for char in s:
            if char=='L':
                lCount+=1
                if rCount==lCount:
                    splittedCount+=1
                    rCount=0
                    lCount=0
            else:
                rCount+=1
                if rCount==lCount:
                    splittedCount+=1
                    rCount=0
                    lCount=0
        return splittedCount