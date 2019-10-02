# 本题思路如下
# By iterating through the string from left to right,
# we can easily determine which row in the Zig-Zag pattern that a character belongs to.
# Iterate through s from left to right,
# appending each character to the appropriate row.
# The appropriate row can be tracked using two variables: the current row and the current direction.
# The current direction changes only when we moved up to the topmost row or moved down to the bottommost row.
class Solution:
    def convert( s: str, numRows: int) -> str:
        #建一个list of strings 每一个string代表一个row
        twoDlist=['' for i in range(numRows)]
        #最开始是往下走的方向
        down=True
        for i in range(len(s)):
            if numRows==1:
                return s
            if i==0:
                twoDlist[0]+=s[i]
            #每到这个时候是往下走在上来又走到第一个row的时候
            elif i%(2*numRows-2)==0 and down==False:
                down=True
                twoDlist[0]+=s[i]
            #每到这个时候是往下走走到了最后一个row的时候
            elif i%(numRows-1)==0:
                down=False
                twoDlist[numRows-1]+=s[i]
            else:
                if down==True:
                    twoDlist[i % (numRows - 1)]+=s[i]
                else:
                    twoDlist[(numRows-1)-i % (numRows - 1)]+=s[i]
        ans=''
        for sub in twoDlist:
            ans+=sub
        return ans
    print(convert('AB',1))