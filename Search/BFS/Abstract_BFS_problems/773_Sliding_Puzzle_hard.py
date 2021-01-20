# 这道题和127题word ladder是同一种类型的，即不是在一个matrix或者tree里进行bfs
# 而是每一个node都代表一种状态，127题里每个node是目前单词的拼写，
# 这道题里每个node是board经过这么多次swap以后到现在的排布
# 而这种问题中，两个node是否相连，就看第二个node是不是第一个node经过一次transformation之后就能得到的
# 127题里就是换一个字母能不能从第一个词到第二个词，如果能，那么两个词就是相连的nodes
# 这道题就是在第一种board的排布的基础上做一次0和邻居的swap能不能得到第二种board的排布，如果能，那么
# 这两种board排布的形态就是相连的node
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 如果input就直接等于target，return 0
        # 这里必须要check以下，因为如果不check，按照下面的算法走，会把本身就等于target的board
        # 里的0和旁边的一个数字swap以下，之后再下一个level再swap回来，所以会return 2
        if board==[[1,2,3],[4,5,0]]:
            return 0
        #找到board里初始形态中0的坐标，之后我们把每一个新遇到的state给push到queue里时
        #也都带着那个state的0的坐标，这样每次pop出来一个state就不需要用nested for loop
        #去找0在哪了
        zeroR=0
        zeroC=1
        for r in range(0,2):
            for c in range(0,3):
                if board[r][c]==0:
                    zeroR=r
                    zeroC=c
        # queue里的每一个element都是一个有3个element的tuple，第一个element是board在这个state下的布局
        # 即2D array，第二个element是0在这个state里的坐标，是一个tuple，第三个element是这个state在BFS
        # 中所处的level
        queue=[(board,(zeroR,zeroC),0)]
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        # 因为list不是hashable的，所以我们要把见过的state，转化成string之后存到set里
        seen={str(board)}
        while queue:
            # 这里r和c就是当前state里0的坐标
            state,(r,c),level=queue.pop()
            # 找到0周围的邻居们
            for d in directions:
                newR=r+d[0]
                newC=c+d[1]
                if newR<0 or newR>=2 or newC<0 or newC>=3:
                    continue
                # list是object，不能直接在list里swap，得先make一个list的copy之后在copy里swap
                boardCopy=[row[:] for row in state]
                boardCopy[r][c]=boardCopy[newR][newC]
                boardCopy[newR][newC]=0
                #如果swap过后的结果就等于target,那么直接return level+1
                if boardCopy==[[1,2,3],[4,5,0]]:
                    return level+1
                #否则把新的state和新state里0的坐标和level push到queue里
                if str(boardCopy) not in seen:
                    seen.add(str(boardCopy))
                    queue.insert(0,(boardCopy,(newR,newC),level+1))
        # 如果queue空了还没见到target，那就说明这个input board是变不成target的，return -1
        return -1