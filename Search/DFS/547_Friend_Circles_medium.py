#这一类题目给的input本质上是一个adjacency matrix，即matrix的row和col代表的是同一组人，比如M[1,1]的值就代表第二个人
#和第二个人自己是不是好朋友。这样类似与adjacent matrix的input在处理上和大海里找小岛那种input是有很大区别的，解题手段也
#因此不同。首先既然row和col指的是同一组人，假设M是nxn的matrix，那么也就是说M描述的也就是这n个人之间的关系，我们
# 只需要一个1D的，size是n的list来keep track of我们已经看过的人就够了。
# 再具体的说
#如果M[2,3]=1,代表第三个人和第四个人是好朋友，
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or len(M)==0:
            return 0
        visited=[0]*len(M)
        count=0
        #这里有一个思想，即在一个friend circle中，我们可以从任何一个人出发，之后access到所有人
        #我们在这个过程中会把access到的所有人在visited中标记成1
        for person in range(0,len(M)):
            #这个if每执行一次，就是traverse整个一个完整的friend circle，所以if一开始就给count+1
            if visited[person]==0:
                count+=1
                visited[person]=1
                stack=[]
                #现在目前的person对应的row里找到第一个col对应的那个人是没有visit的，且col的value是1的人
                for other in range(0,len(M)):
                    if visited[other]==0 and M[person][other]==1:
                        stack.append(other)
                        visited[other]=1
                        #之后用这个while loop来穷尽所有在这个friend circle里的人
                        while stack:
                            newPerson=stack.pop()
                            for newOther in range(0,len(M)):
                                if visited[newOther]==0 and M[newPerson][newOther]==1:
                                    stack.append(newOther)
                                    visited[newOther]=1
        return count
#这里讨论一下这个方法的时间复杂度，看似是一个一共有四个loop套在一起，但是实际上，因为visit过的会在之后的traversal中
#被直接跳过，所以M的每个位置都只被visit过一次，因此对于nxn的M而言时间复杂度是O（n^2），空间复杂度也是O(n^2)因为
#在极端的所有人和所有人都是朋友的情况下，stack里最多的时候几乎会有全部的n^2个位置

#下面是这道题的recursive implementation
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [0] * len(M)
        count = 0

        def _dfs(visited, person):
            for other in range(0, len(M)):
                if visited[other] == 0 and M[person][other] == 1:
                    visited[other] = 1
                    _dfs(visited, other)

        for person in range(0, len(M)):
            if visited[person] == 0:
                count += 1
                visited[person] = 1
                _dfs(visited, person)

        return count