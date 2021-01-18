# 想理解这道题得先理解144题，post_order直接用iterative写写不出来
# iterative只有在node itself是第一个被access的时候才成立
# 我们知道post order的顺序是 left right nodeitself
# 那么我们可以把它的顺序调过来求出 nodeitself right left的结果 再在return是把这个结果整体reverse
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            # because for the leaf nodes, we push None as their left and right into the stack
            # we don't want to include None in our result
            # so is the node popped out by the stack is None, we do nothing
            if node:
                res.append(node.val)
                # 为了让右边的先被pop 我们先push左 再push右
                stack.append(node.left)
                stack.append(node.right)
        # 对于res[::-1] 到底是怎么回事，具体看这个
        # https://stackoverflow.com/questions/13365424/what-does-result-1-mean
        return res[::-1]

#以下是用纯iterative的方法，不像上面一样改变顺序那样解的
#以后如果看不懂的话，看这个视频 https://www.youtube.com/watch?v=xLQKdq0Ffjg
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        res=[]
        curr=root
        while curr or stack:
            #进来以后先找到目前所在这个branch的最左边的node，
            #这里说的是最左面的，但不一定是最左下的，因为这个node虽然没有left child了，但是可能有right child
            #直到某一刻，curr指向的是那个没有left child的node的left，即None，这时进入下面的else
            if curr:
                stack.append(curr)
                curr=curr.left

            else:
                #这里的temp实际上有两种情况：
                #1.按照上面所说的那种进到else的情况，stack[-1]是那个没有left child的node A
                #那么temp是A的right child，这里temp可能是None，所以有了下面的一组if else来讨论temp是不是None的情况
                #先看下面if else的comment，看完在回来看下面的第二种情况
                #2.好像应该没有第二种情况了
                temp=stack[-1].right
                #如果temp是None，那说明node A没有right child，上面我们已经确定了它没有left child
                #所以它就是当前branch最左下角的node了，按照postorder的定义，该把它放进res了
                if not temp:
                    temp=stack.pop()
                    res.append(temp.val)
                    #把它放进了res以后，我们在stack不为空的前提下，我看node A是不是它的parent node的right child
                    #首先我们刚才让temp=stack.pop()了 被pop出来的就是node A，且这里stack[-1]是A的parent node
                    #如果node A就是它的parent的right child的话，它自己没孩子，它自己也进了res了，那说明它的parent
                    #的左右child都处理完了，该处理它的parent自身了，所以这时我们把它的parent pop出来，让temp等于它
                    #并把它的val加入res。注意这个过程在这是循环的，只要stack不空且temp是自己的parent的right child
                    #就该处理temp的parent自身了。这个while loop会连续走很多次的例子是针对一个一串单传的，并且每个node
                    #都是自己的parent的right child的情况

                    #当temp不是它的parent的right child时，那它就是parent的left child，那么我们的下一步就是看parent有没有right child
                    # 在程序中我们会进入整个大while的下一次循环，因为cur这时指向的还是空
                    #所以在这一次新的while循环中我们会直接进入38行的else，再一次开始判断目前stack的最后一位有没有right child
                    while stack and temp==stack[-1].right:
                        temp=stack.pop()
                        res.append(temp.val)
                #如果temp不是None，这里temp还是A的right child呢，那证明A还有right child，直接让curr等于temp
                #相当于开启了对于一个新的branch的探索
                else:
                    curr=temp
        return res