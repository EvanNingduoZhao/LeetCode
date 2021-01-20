# 在graph theory中对于tree的定义是需要满足以下两个条件
# 1. 得是fully connected，即我们从一个node开始DFS，能过reach到所有其他nodes
# 2. 内部不能有cycles，也就是说我们在DFS的过程中不能重复经过一个node两次，但是这里要注意不能被
# trivial cycle给迷惑了，什么是trivial cycle。我们这道题是一个undirected graph
# 也就是说1和2两个node之间的edge其实是1到2 和2到1两个方向都可以，那么一个trivial cycle
# 就是1->2->1，如果我们不采取措施的话，在DFS的过程中就会陷入这种trivial cycle，
# 导致我们以为自己到了1这个node两次，从而错误地判断这个graph不是一个合格的tree

#那么该采取什么措施呢？ 看下面code的comment
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 如果只有一个node且edges为空，那这就是一个只有一个root的tree，是合格的
        #但是如果有超过一个node，还edges为空，那就不是fully connected了
        if not edges or len(edges)==0:
            if n==1:
                return True
            else:
                return False
        # 想用dfs，我们先要build一个ajdaceny list
        # adjacency list就是一个dict，key是每一个node，value是这个一个list里面存着所有和这个key node
        # 相连的node。
        # 同时还有一种东西叫adjacency matrix，那种是这样的：假设我们有V个node，那么就是一个V*V的matrix
        # 如果i node和j node是相连的那么matrix[i][j]的值就是1，如果不相连值就是0
        # 只有edges的数量远大于node的数量时（每个node都和很多个其他node相连），
        # 用adjacency matrix才有意义，因为adjacency matrix占的space是V square，但是ajdaceny list
        # 占的space是V+E，这里E是edge的数量。就是V+E，这么记就行了
        adjacency={}
        for e in edges:
            if e[0] not in adjacency:
                adjacency[e[0]]=[e[1]]
            else:
                adjacency[e[0]].append(e[1])
            if e[1] not in adjacency:
                adjacency[e[1]]=[e[0]]
            else:
                adjacency[e[1]].append(e[0])
        stack=[edges[0][0]]
        seen={edges[0][0]}
        while stack:
            node=stack.pop()
            for nei in adjacency[node]:
                if nei in seen:
                    return False
                stack.append(nei)
                seen.add(nei)
                # 假设2这个node是作为1的邻居被我们发现的，那么我们这里就要在把2push到stack里以后
                # 把1从2的neighbor里去掉，这样就不会在处理2的邻居时，因为trial cycle而再次遇到1了
                adjacency[nei].remove(node)
        # seen是一个set，因此如果seen的size和node的数量相等，那就说明所有的node我们都经过了，是fully connected
        if len(seen)==n:
            return True
        #反之则return false
        else:
            return False

# 实际上如果我们在tree的定义上再做一个推论的话，就会发现没有cycle其实就等于一个n个node的graph
# 想要是tree的话，只能有n-1个edge，且n个node fully connected。为什么是n-1个edge呢？因为n个node
# 想要fully connected 就至少需要n-1个edge，但是只要多余n-1个edge了就说明有cycle

# 因此我们的判定条件可以简化为以下两个标准，1. fully connected 2. 有且只有n-1个edges
# 这样的话，我们只需要在开头check以下edges这个list的size是不是等于n-1，再看seen的size是不是等于n就够了
# 不需要考虑 cycle和trivial cycle那些东西了（不需要remove了）

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #check以下edges这个list的size是不是等于n - 1
        if len(edges) != n - 1:
            return False
        if not edges or len(edges)==0:
            if n==1:
                return True
            else:
                return False
        adjacency={}
        for e in edges:
            if e[0] not in adjacency:
                adjacency[e[0]]=[e[1]]
            else:
                adjacency[e[0]].append(e[1])
            if e[1] not in adjacency:
                adjacency[e[1]]=[e[0]]
            else:
                adjacency[e[1]].append(e[0])
        stack=[edges[0][0]]
        seen={edges[0][0]}
        while stack:
            node=stack.pop()
            for nei in adjacency[node]:
                if nei in seen:
                    continue
                stack.append(nei)
                seen.add(nei)
        if len(seen)==n:
            return True
        else:
            return False