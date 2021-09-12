# 这道题本质上和547题是一摸一样的，只不过这道题需要先自己根据edges搭建一个adjacency matrix
# 注意一个心法，对于这种undirected graph，即如果A和B之间有edge，那么算A连着B，也算B连着A
# 对于这种undirected graph，要用adajcency matrix来记录
# 剩下的都和547一样的，下面也是介绍了iterative和recursive的解法

# iterative dfs solution
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adajcency = [[0 for i in range(n)] for j in range(n)]
        for edge in edges:
            adajcency[edge[0]][edge[1]]=1
            adajcency[edge[1]][edge[0]]=1
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                count+=1
                visited.add(i)
                stack = []
                for j in range(i+1,n):
                    if j not in visited and adajcency[i][j]==1:
                        stack.append(j)
                        visited.add(j)
                        while stack:
                            node = stack.pop()
                            for newNeighbor in range(i+1,n):
                                if newNeighbor not in visited and adajcency[node][newNeighbor]==1:
                                    stack.append(newNeighbor)
                                    visited.add(newNeighbor)
        return count

# recursive dfs solution
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adajcency = [[0 for i in range(n)] for j in range(n)]
        for edge in edges:
            adajcency[edge[0]][edge[1]] = 1
            adajcency[edge[1]][edge[0]] = 1
        count = 0
        visited = set()

        def dfs(node, visited):
            for i in range(n):
                if i not in visited and adajcency[node][i] == 1:
                    visited.add(i)
                    dfs(i, visited)

        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i, visited)
        return count

# 不成熟的写法 不用看
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeDict = {}
        count = 0
        seen = set()
        for edge in edges:
            if edge[0] in edgeDict:
                edgeDict[edge[0]].append(edge[1])
            else:
                edgeDict[edge[0]] = [edge[1]]
            if edge[1] in edgeDict:
                edgeDict[edge[1]].append(edge[0])
            else:
                edgeDict[edge[1]] = [edge[0]]
        # print("edgeDict is:", edgeDict)
        for i in range(n):
            if i not in seen:
                if i in edgeDict:
                    # print("i is:", i)
                    seen.add(i)
                    stack = [n for n in edgeDict[i]]
                    # print("stack is:", stack)
                    while stack:
                        node = stack.pop()
                        # print("node is:",node)
                        seen.add(node)
                        if node in edgeDict:
                            for newNode in edgeDict[node]:
                                if newNode not in seen:
                                    stack.append(newNode)
                    count+=1
        # print("seen is:", seen)
        return count+n-len(seen)