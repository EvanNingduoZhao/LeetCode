#这道题是用BFS在grid中找最短路径的经典题目，必须要会
#这个视频里讲解的是这道题的一个稍微简化版的题目，但是思路是一样的，
#   https://www.youtube.com/watch?v=KiCBXu4P-2Y
#可以从大概7分钟的地方开始看，前7分钟主要是将direaction vector的
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        #如果左上和右下作为起点和终点的位置的value是1的话，那当然是没有path的了
        if not grid or grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        else:
            #这个是专门处理grid只有一个位置，且这个位置的值是0的情况的
            if len(grid) == 1:
                return 1
            #后面会用8个direction vectors来找一个位置的所有neighbor
            neighbors = [[0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1]]
            #BFS traversal要用queue
            queue = [([0, 0], 1)]
            while queue:
                #queue里存的是tuple，tuple的第一个element是一个list，即位置的坐标，第二个element是一个数字
                #即该位置离起点的距离（该位置在相对于起点的第几层）
                #这里要讨论一个问题，假设当前我们说的位置是A点，从起点走到A点可能有很多中走法，每种所take的步数都可能不同
                #那么我们在tuple的第二个element里存的是那种从起点到A点的走法呢？答案是由BFS走出来的走法，即最短的走法
                #那么为什么BFS给出的就一定是最短的呢？
                #因为BFS工作的方式是，离起点距离是1的位置都归第一层，离第一层里的位置距离是1的所有位置（刨除已经visit过的）
                # 都归第二层，离第二层里的位置距离是1的所有位置（刨除已经visit过的）都归第三层，以此类推
                # 每个位置都是最先被通过从起点到达它的最短的那条路径找到的，之后被标记成visited，那么就算之后有更长一些
                #的路径可以从起点到达它，但是那时它已经被标记成visited，不需要再管它了
                #因此每个位置在BFS中所处的层数就代表了从起点到达它的最短路径的长度
                #最后再啰嗦一个问题，如果一个位置是从某个第二层的位置走一步就能到的，那它离起点的距离一定是3
                #因为如果它离起点的距离是1或者2的话，它在前面就会被归到第一层或者第二层了。更不可能是4，距离起点是
                #2的一个位置走一步就到达你，那你离起点的距离最远也就是3了
                curr_position, curr_step = queue.pop()
                #通过direction vector来找到curr_position的每个neighbor
                for neighbor in neighbors:
                    #通过把curr_position的坐标和direction vector的坐标相加得到neighbor的坐标
                    pos = [sum(x) for x in zip(curr_position, neighbor)]
                    #如果这个neighbor就是终点的话，直接return curr——position的层数+1，因为curr position的邻居的层数是要
                    #比它高一层的。注意这里的道理就是刚才上面所说的，在一个位置被BFS第一次发现时，那么这一路上经过的路径就是
                    #从起点到达它的最短路径
                    if pos == [n - 1, n - 1]:
                        return curr_step + 1
                    #如果邻居的坐标里有一个值是小于0或者大于n-1的话，那它不是一个valid的坐标，直接continue
                    if pos[0] < 0 or pos[1] < 0 or pos[0] > n - 1 or pos[1] > n - 1:
                        continue
                    #如果当前邻居的值是1的话也continue，值是1可能是本来就是1，下面的code会看到，我们把所有visited过的
                    #位置的值也都标成1，所以值是1也可能是因为被visit过了，不管哪种情况都是要跳过它
                    if grid[pos[0]][pos[1]] == 1:
                        continue
                    #对于valid的neighbor，且又不是直接就是终点的，我们把它push到queue里
                    queue.insert(0, (pos, curr_step + 1))
                    #同时这里按照上面所说的，被push到queue里就算是被visit过了，所以把它的值标成1
                    #push到queue里的目的是为了之后把它pop出来找它的邻居，即下一层的位置，对于它自己而言，被push进
                    #queue之前就算是被visit过了
                    grid[pos[0]][pos[1]] = 1
            #如果在queue空了，整个while loop结束了以后还没碰到终点，那就说明没有路径可以从起点到终点，return -1
            return -1
