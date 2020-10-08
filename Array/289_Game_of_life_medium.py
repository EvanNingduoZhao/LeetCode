#这道题其实不难，甚至有点配不上medium的难度
#这道题最关键的一个要想明白的地方就是题目中说的simultaneous update,
# simultaneous update要求的是，每一个位置的值的update都要根据board在最初始的状态下每个位置的值来进行，
# 即在iterative traversal时，不能数完了一个
#位置的邻居里有几个是活着的就直接相应的update那个位置的值，因为这样我们就丢失了那个位置原来的值，那么在那个位置作为
#别人的邻居时，我们就不知道它在原始的board中的值是什么了。为了存好每个位置的原始值，我们可以新建一个board来存它们
#但是这道题的follow up 1是要求用O(1) space来解决这个题，那么我们就可以采用下面的code中我用的这个办法：
#即要把0 update成1时，不直接update成1，而是update成2，这样所有后变成1的位置的值都是2，这就能够和原始值就是1的位置
#进行区分了，同理，要把1update成0时也不直接update成0，而是update成-1，这样我们就知道，这个地方虽然现在的值应该是0
#但是这里的原始值其实是1。这样一来我们在数一个位置的邻居有几个原本是1时，就应该只算目前值是1（原始就是1）或者是-1
# （原始是1被update成0的）的
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        m = len(board)
        n = len(board[0])
        for r in range(m):
            for c in range(n):
                counter = 0
                for d in directions:
                    newRow = r + d[0]
                    newCol = c + d[1]
                    #出界的坐标直接跳过
                    if newRow < 0 or newRow >= m or newCol < 0 or newCol >= n:
                        continue
                    if board[newRow][newCol] == 1 or board[newRow][newCol] == -1:
                        counter += 1
                #每个位置都是在（r，c）对应的是自己时才会被update
                #所以board[r][c]指的位置的值一定都是还没有被update过的，
                #所以值要么是1要么是0，不会有2和-1出现
                #讨论自己是1时的三种条件
                if board[r][c] == 1:
                    if counter < 2:
                        board[r][c] = -1
                    elif counter == 2 or counter == 3:
                        continue
                    else:
                        board[r][c] = -1
                #讨论自己是0时的一种条件
                else:
                    if counter == 3:
                        board[r][c] = 2
        #最后才从头到尾过一遍 把2换成1，把-1换成0
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == -1:
                    board[r][c] = 0
                else:
                    continue
        return board
