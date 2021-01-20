#这道题应该可以很容易判断出来是BFS问题，因为坏了的橘子每一分钟都只能感染它邻居的好橘子
#那么实际上没一分钟后新被感染的橘子就是BFS的一个新的level，最后在BFS queue空了的时候，如果
#开始时所有的好橘子都被感染了，那么就return目前见过最大的level数
#如果不是所有的好橘子都被感染了，说明好橘子里有在孤岛上的，那么return -1

#这就要求我们在算法的最开始用nested forloop过一遍grid，把所有坏橘子的坐标存起来
#并且数出来，开始时好橘子有多少个
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or len(grid)==0 or len(grid[0])==0:
            return -1
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        rotten=[]
        freshCount=0
        m=len(grid)
        n=len(grid[0])
        #用nested forloop过一遍grid，把所有坏橘子的坐标存起来
        # 并且数出来，开始时好橘子有多少个
        for row in range(0,m):
            for col in range(0,n):
                if grid[row][col]==2:
                    # 因为我们要keep track of 最大的level，所以开始就是坏的橘子我们让他的level是0
                    # 这里rotton这个queue里每个element是一个tuple，tuple的第一个element还是一个tuple
                    # 存着该橘子在grid里的坐标，第二个element是该橘子的level数
                    rotten.append(((row,col),0))
                if grid[row][col]==1:
                    freshCount+=1
        largestLevel=0
        # 记录从开始以后新感染了多少个开始时是好的橘子
        newRottonCount=0
        while rotten:
            (r,c),level=rotten.pop()
            for d in directions:
                newRow=r+d[0]
                newCol=c+d[1]
                if newRow<0 or newRow>=m or newCol<0 or newCol>=n:
                    continue
                if grid[newRow][newCol]==1:
                    # 好的橘子被感染了以后标成2，这样就不会重复visit
                    newRottonCount+=1
                    grid[newRow][newCol]=2
                    rotten.insert(0,((newRow,newCol),level+1))
                    largestLevel=max(largestLevel,level+1)

        #最后在BFS queue空了的时候，如果
        # 开始时所有的好橘子都被感染了，那么就return目前见过最大的level数
        # 如果不是所有的好橘子都被感染了，说明好橘子里有在孤岛上的，那么return -1
        if newRottonCount==freshCount:
            return largestLevel
        else:
            return -1