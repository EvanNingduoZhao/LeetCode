#这道题本质上和大海里找小岛还是差不多的
#但是多了两个components，第一个是在travserse每一块O的区域时，都要用一个flag variable 来keep track of
#这个area里的O里面有没有在border上的O，如果有的话，那这一块区域就没有资格被换成x了
#第二个是在traverse一个O区域时，除了用一个stack以外还需要用一个additional的list来keep track of这一块区域里一共都有
#那些位置，只有这样，在traverse完了这片区域以后才能知道这片区域里一共都有谁，如果要把这片区域都换成x的话，才知道哪些要换
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board)==0 or len(board[0])==0:
            return
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        rows=len(board)
        cols=len(board[0])
        #把visited全部initialize成0
        #这里因为含有border的O的O区域是不能被换成X的，所以不能通过inplace mark的方式来keep track of visited的位置
        visited=[[0 for _ in range(cols) for _ in range(rows)]]
        for r in range(0,rows):
            for c in range(0,cols):
                if board[r][c]=='O' and visited[r][c]==0:
                    stack=[(r,c)]
                    #additional的list来keep track of这一块区域里一共都有哪些位置
                    currArea=[(r,c)]
                    #用来keep track of 这片O区域里有没有border上的O的flag
                    containBoarder=False
                    visited[r][c]=1
                    while stack:
                        currRow,currCol=stack.pop()
                        if currRow==0 or currCol==0 or currRow==rows-1 or currCol==cols-1:
                            containBoarder=True
                        for d in directions:
                            newRow=currRow+d[0]
                            newCol=currCol+d[1]
                            if newRow>=0 and newRow<rows and newCol>=0 and newCol<cols:
                                if board[newRow][newCol]=='O' and visited[newRow][newCol]==0:
                                    stack.append((newRow,newCol))
                                    currArea.append((newRow,newCol))
                                    visited[newRow][newCol]=1
                    #只有不contain border上的O的O区域才能有资格被换成x
                    if not containBoarder:
                        for rArea,cArea in currArea:
                            board[rArea][cArea]='X'

#下面的是标准答案里的DFS方法，这个方法相较于上面自己的方法做出了如下几个优化：
#1. 这个方法没有对所有的O区域都进行DFS，而是只从border上的O开始进行DFS，并把所有和border上的O连接的O都标成E
#等所有border上的O的DFS都进行完了以后，我们从头到尾traverse整个board，把所有的O换成X，把所有的E换成O
#2. 因为在这个方法中，我们把所有和border的O相连的O都标成了E，这就相当于是inplace mark visite过的了，因此不需要额外的
# list来keep track of visited的位置
#3.这个方法没有在DFS内部进行boundary check（即对于每个位置我都一定要把四个邻居都看一遍，就算有的邻居在board外面也得看）
#而是根据每个位置自己的位置，来决定要对自己的哪些neighbor来call dfs（感觉这个实际上不是很重要的优化）
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        self.ROWS = len(board)
        self.COLS = len(board[0])

        # Step 1). retrieve all border cells
        from itertools import product
        borders = list(product(range(self.ROWS), [0, self.COLS-1])) \
                + list(product([0, self.ROWS-1], range(self.COLS)))

        # Step 2). mark the "escaped" cells, with any placeholder, e.g. 'E'
        for row, col in borders:
            self.DFS(board, row, col)

        # Step 3). flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O':   board[r][c] = 'X'  # captured
                elif board[r][c] == 'E': board[r][c] = 'O'  # escaped


    def DFS(self, board, row, col):
        if board[row][col] != 'O':
            return
        board[row][col] = 'E'
        if col < self.COLS-1: self.DFS(board, row, col+1)
        if row < self.ROWS-1: self.DFS(board, row+1, col)
        if col > 0: self.DFS(board, row, col-1)
        if row > 0: self.DFS(board, row-1, col)