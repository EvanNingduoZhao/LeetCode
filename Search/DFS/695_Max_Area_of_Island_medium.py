#BFS的特点是一层一层traverse的，所以适用于求最短距离，最少步骤这一类的问题。而这道题问的其实是相当于，在找到一个
#value是1的postion A以后，怎么样能够遍历属于这个岛的所有position，这就要用DFS，先把A周围四个方向的四个position都看一下
#把value是1的都append到一个stack里，再从stack里挨个pop出来，把新pop出来的position周边value是1的position再push到stack里
#去，这样保证了可以遍历整个岛的所有位置（每把一个新的位置append到stack里就给currArea加1，这样最后currArea就是这个岛的面积）。
# 这里我们还用了一个经典的方法俩避免重复count，即每次把一个position append到stack里以后就把它的value从1改成0，因为我们是不会
#把value是0的position放到stack里的，这样就避免了重复count。如果题目中不允许modify input的话，那么我们可以用一个set来存
#所有已经看过的position，每次见到一个value是1的position首先check它是不是在set里，只有不在set里时，说明之前没见过，
#才能push到stack里。check一个value在不在一个set里average take O(1)。也可以用一个boolean array，大小和input一样，只要
#看过一个position就把boolean array的对应位置标成True。用set和boolean array没啥区别，对于实现check一个位置有没有被看过
#这个功能都是用了time O(1),space O(n).
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #check edge case
        if not grid or len(grid)==0 or len(grid[0])==0:
            return 0
        stack=[]
        maxArea=0
        #direction vector的小trick用来代表四个方向
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        #我们这里用一个nested for loop来traverse整个grid，这个nested for loop同时也是我们这个function的driver
        #首先我们在traversal中一行一行一个位置一个位置挨个找，直到找到第一个value是1的position，把它push到stack里去
        #之后能我们用while loop进行一个经典的DFS，直到traverse里了属于这个岛的每一个position。且在traverse的过程中
        #这个岛的每一个position的value都变成0了，相当于岛就变成了大海。那么对于这一个岛结束了以后，我们的nested for loop
        #继续进行，继续一行一行一个位置一个位置traverse，直到找到下一个value是1的position，在找到下一个value是1的position
        #之前，我们可能还会再次经过之前已经explore过的岛的position，但是由于它们的value都被我们改成0了，所以我们并不会
        #为它们停在脚步，我们再次看到的value是1的position一定是属于我们还没有explore过的岛的。
        for row in range(0,len(grid)):
            for col in range(0,len(grid[0])):
                if grid[row][col]==1:
                    stack.append((row,col))
                    currArea=1
                    maxArea=max(maxArea,currArea)
                    grid[row][col]=0
                    while stack:
                        currRow,currCol=stack.pop()
                        #挨个检查四个方向上的邻居
                        for d in directions:
                            newRow=currRow+d[0]
                            newCol=currCol+d[1]
                            #保证邻居的坐标是valid的，没有出界的
                            if newRow<0 or newRow>len(grid)-1:
                                continue
                            if newCol<0 or newCol>len(grid[0])-1:
                                continue
                            if grid[newRow][newCol]==1:
                                stack.append((newRow,newCol))
                                currArea+=1
                                maxArea=max(maxArea,currArea)
                                grid[newRow][newCol]=0
        return maxArea

#总结，如果这个2D list上一共用n个位置的话，这个方法的space compleixty是O(n)因为我们用一个stack来存位置，
#time complexity也是O(n)，因为对于每一个位置而言我们只会access它最多两次，第一次是它作为1被第一次发现时
#第二次是它的value被改成0了以后nested for loop第二次经过它时。