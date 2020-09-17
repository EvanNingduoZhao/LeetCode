class Solution:
    # 自己写的接近O（n）的方法，但是如果用的不是list 而是hashtable就效率更高了
    # hashtable的方法见下面
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        count=0
        stack=[(root,[root.val])]
        while stack:
            node,sums=stack.pop()
            for s in sums:
                if s==sum:
                    count+=1
            if node.left:
                new_sums=[s+node.left.val for s in sums]
                new_sums.append(node.left.val)
                stack.append((node.left,new_sums))
            if node.right:
                new_sums=[s+node.right.val for s in sums]
                new_sums.append(node.right.val)
                stack.append((node.right,new_sums))
        return count

    # double recursion 这其实是一种brute force
    # double recursion 其实也是一种基本的算法思想但是不是很常见
    # inner recursion 也就是helper function的作用是：
    #   以某一个node 为root，找到所有以这个node为起点的path sum等于sum的path
    #   这个inner recursion的思想和112题Path_sum的recursion做法基本是一样的
    #   只不过这里不是遇到了第一个符合条件的path就return True而是用一个count来记录遇到的所有符合条件
    #   的path的数量
    # outer recursion的作用是让所有node都当一次root
    # 这个方法的youtube讲解：https://www.youtube.com/watch?v=NTyOEYYyv-o
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # edge case
        if not root:
            return 0
        # inner recusion
        def helper(root, sum):
            count = 0
            if not root:
                return 0
            if root.val == sum:
                count += 1
            # 要想明白这个count具体是怎么加上去的
            count += helper(root.left, sum - root.val)
            count += helper(root.right, sum - root.val)
            return count
        # outer recursion
        return helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


    # 以下是上面提到的用hashtable的最优办法
    # A more efficient implementation uses the Two Sum idea.
    # （two sum idea是在之间做list的题的时候学到的思路：
    # 即在目标是找到两个合在一起可以满足某条件的两个elements的时候
    # 每碰到一个新的new_element就把它放到hashtable里，并在已有的hashtable里找有没有跟这个new_element合在一起
    # 就可以满足给定条件的element.Two sum是hashtable的一个典型用法）
    # It uses a hash table (extra memory of order N).
    # With more space, it gives us an O(N) time complexity.

    # As we traverse down the tree, at an arbitrary node N,
    # we store the sum until this node N (sum_so_far (prefix) + N.val).
    # in hash-table. Note this sum is the sum from root to N.
    # Now at a grand-child of N, say G, we can compute the sum from the root until
    # G since we have the prefix_sum until this grandchild available.We pass in our
    # recursive routine.

    # How do we know if we have a path of target sum which ends at this grand-child G?
    # Say there are multiple such paths that end at G and say they start at A, B, C
    # where A,B,C are predecessors of G. Then sum(root->G) - sum(root->A) = target.
    # Similarly sum(root->G)-sum(root>B) = target. Therefore we can compute the complement
    # at G as sum_so_far+G.val-target and look up the hash-table for the number of paths
    # which had this sum

    # Now after we are done with a node and all its grandchildren, we remove it from the
    # hash-table. This makes sure that the number of complement paths returned always
    # correspond to paths that ended at a predecessor node.
    # 这个方法的讲解：https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result = 0

        self.helper(root, sum, 0, {0: 1})
        return self.result

    def helper(self, root, target, so_far, cache):
        #看了上面的英文就可以知道，在helper里我们找到的是以root为结尾的合适的path
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            # dict.setdefault（key，v）这个function是这么回事
            # 如果key已经在dict里了，return目前dict里key对应的value
            # 如果key不在dict里，则在dict里加入（key，v）这个key value pair并return v
            cache.setdefault(so_far + root.val, 0)
            # 上一行先试探一下so_far+root.val这个key是不是已经在cache这个dict里面了
            # 如果没在的话先把(so_far + root.val, 0)这个key value pair放进去
            # 这样cache[so_far + root.val] += 1不会因为cache里没有so_far + root.val这个key而报错
            cache[so_far + root.val] += 1
            self.helper(root.left, target, so_far + root.val, cache)
            self.helper(root.right, target, so_far + root.val, cache)
            #当一个node的所有子孙都被当作path的结尾遍历过一次以后就要把这个node对应的那个key的value减1
            # （把这个node从hashtable里拿掉）
            # 因为从此以后再遇到的new_node都不会再是这个node的子孙了，那么这个node也不可能是
            # 以再新遇到的new_node为结尾的合格的path的开头了，因此就算以到新遇到的new_node为止的path sum
            # 的complement是以这个node为止的path sum，那也不能算在result里了。所以要把对应的value-1
            cache[so_far + root.val] -= 1
        return

    #以下这个code是2020.9 复习时自己重写的上面那个method,这个code是怎么会是直接参照上面的code的comment就好
    class Solution:
        def pathSum(self, root: TreeNode, sum: int) -> int:
            self.counter = 0
            self.record = {}
            self.target = sum
            self._helper(root, 0)
            return self.counter

        def _helper(self, root, curr_sum):
            if not root:
                return
            else:
                curr_sum += root.val
                if curr_sum == self.target:
                    self.counter += 1
                if curr_sum - self.target in self.record:
                    self.counter += self.record[curr_sum - self.target]
                if curr_sum in self.record:
                    self.record[curr_sum] += 1
                else:
                    self.record[curr_sum] = 1
                self._helper(root.left, curr_sum)
                self._helper(root.right, curr_sum)
                self.record[curr_sum] -= 1