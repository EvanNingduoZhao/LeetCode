# 这道题需要我们先用nested for loop找到其中一个小岛的一片地方，之后用DFS从这一个地方开始
# 找到所有属于这个岛的地方，这里我们在DFS的过程中还把这个岛的地方的值都换成-1
# 并且把所有属于这个岛的位置的坐标都存到firstIsland这个list里
class Solution:
    def shortestBridge(self, A):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        stack = []
        firstIsland = []
        n = len(A)
        m = len(A[0])
        for row in range(0, n):
            for col in range(0, m):
                if A[row][col] == 1:
                    A[row][col] = -1
                    stack.append((row, col))
                    firstIsland.append((row, col))
                    break
            # 以下这三行是用来让17行的break能直接break出两层nested for loop的，这个写法是python的定式，要记住
            else:
                continue
            break

        # 找到所有属于这个岛的地方，这里我们在DFS的过程中还把这个岛的地方的值都换成-1
        # 并且把所有属于这个岛的位置的坐标都存到firstIsland这个list里
        while stack:
            r, c = stack.pop()
            for d in directions:
                newR = r + d[0]
                newC = c + d[1]
                if newR < 0 or newR >= n or newC < 0 or newC >= m:
                    continue
                if A[newR][newC] == 1:
                    stack.append((newR, newC))
                    firstIsland.append((newR, newC))
                    A[newR][newC] = -1
        # 把第一个岛上的所有位置都放一个queue里，这个queue里的每个element是一个tuple
        # tuple的第一个element还是一个tuple，即坐标，第二个element是这个位置相对于第一个岛的层数
        # 对于本身就在第一个岛里的位置，我们认为层数是0
        # 我们以整个第一个岛上的所有位置作为queue的起始内容，那么在之后的某一个时刻，这些起始内容会被
        # 都pop出去了，之后queue里剩下的全是level是1的位置，即岛周围的一圈位置
        # 再之后的某一个时刻，queue里剩下的会全是level是2的位置，以此类推，直到queue里的一个位置碰到了第二个岛为止
        queue = []
        for pos in firstIsland:
            queue.insert(0, (pos, 0))
        while queue:
            (r, c), level = queue.pop()
            for d in directions:
                newR = r + d[0]
                newC = c + d[1]
                if newR < 0 or newR >= n or newC < 0 or newC >= m:
                    continue
                if A[newR][newC] == 0:
                    queue.insert(0, ((newR, newC), level + 1))
                    A[newR][newC]=2
                if A[newR][newC] == 1:
                    #注意这里我们没有return level+1，这个位置的level实际上是应该等于level+1
                    #但是因为题目问的是桥得多长，这里以及是第二个岛上的位置了，因此桥的长度应该是
                    #等于level
                    return level
