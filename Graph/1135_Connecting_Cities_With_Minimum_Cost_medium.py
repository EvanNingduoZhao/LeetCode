# 这道题是一个典型的minimal spanning tree(MST)问题，解决MST问题需要背下来这个Kruskal算法
# 这个K算法实际上比较简单，需要三步：
# 1. Sort all the edges in non-decreasing order of their weight.
# 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
# 3. Repeat step#2 until there are (V-1) edges in the spanning tree.
# 这道题不保证给的connections一定能形成一个MST，所以我们的第三步和经典K算法的第三步有些区别
# K算法的第二步要check目前在看的edge加到spanning tree formed so far里以后会不会导致出现一个cycle
# 我们就用union find来实现这个check

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        #parent[i]里记录是城市i的parent是谁
        parents = [i for i in range(0, n + 1)]
        # ranks[i]记录的是以城市i为root的这个tree里一共有几个node
        ranks = [1 for i in range(0, n + 1)]

        # find这个function是用来找n这个城市的root的
        # root node是自己的parent就是自己
        def find(n):
            # 我们要找的是那个自己的parent就是自己的node
            # 如果n != parents[n]，那么n就肯定不是root
            while n != parents[n]:
                # 这里进行了一个path compression。path compression的目的是让一个tree里的node
                # 尽量都直接连到这个tree的root上，这样find每个node的root就会很快，因为不需要
                # 往上找很多层了
                # 既然n自己不是root，那么n的爸爸有可能是root，也有可能n的爷爷或者更高的祖先是root
                # 为了compress path
                # 我们这里让n记录在册的爸爸变成n之前记录在册的爷爷(parents[parents[n]]是n的爷爷)
                # 为什么可以这样的呢，因为如果n的爸爸就是root的话，那个n的爸爸的爸爸应该还是n的爸爸自己
                # 因为root的爸爸是自己。所以再这种情况下，n的爷爷和n的爸爸是一个node，因此让n记录在册
                # 的爸爸变成n记录在册的爷爷本质上是没变，所以下一行n = parents[n]还会让n等于真正的root
                # 如果n的爸爸不是root，root是n更高的祖先，那这么做就更没问题了，
                parents[n] = parents[parents[n]]
                n = parents[n]
            # 最后return找到的root
            return n

        def union(p, q):
            rootP = find(p)
            rootQ = find(q)
            # 如果p和q的root是同一个node，那说明它俩本身就再一个tree里不需要union了
            if rootP == rootQ:
                return True
            # 如果它俩的root不是同一个node，那么需要union它俩所在的两个tree
            # 具体操作是我们要让size更小的那个tree的root认size更大的那个tree的root做爸爸
            # 并且注意更新ranks里关于tree的size的记录
            if ranks[rootP] > ranks[rootQ]:
                parents[rootQ] = rootP
                ranks[rootP] += ranks[rootQ]
            else:
                parents[rootP] = rootQ
                ranks[rootQ] += ranks[rootP]
            # 如果需要union要return False
            return False

        # 根据cost从小到达sort connections
        connections.sort(key=lambda x: x[2])
        totalCost = 0
        # 从小到大traverse connections
        for x, y, cost in connections:
            # 如果union(x,y)return的是True，那说明x和y本身就在同一个tree里，那么如果再
            # connect x和y这两个城市就会造成cycle了，所以再那种情况下我们不把x和y之间的connection
            # 放进我们的spanning tree。只有return False，说明他俩本身不在一个tree里时才可以把
            # 他俩之间的connection放到spanning tree里
            if union(x, y) == False:
                totalCost += cost
        # 如果我们形成了一个MST的话，那么所有的node的root应该都是同一个，那么下面commonRoot这个set的size
        # 应该就是1
        commonRoot = {find(x) for x in range(1, n + 1)}
        return totalCost if len(commonRoot) == 1 else -1