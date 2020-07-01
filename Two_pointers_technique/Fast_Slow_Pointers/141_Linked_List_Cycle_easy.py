# 我给这个方法起名叫快慢指针赛跑法
# 如果一个linked list有circle的话，那么这两个一快一慢的选手早晚会都跑到circle里，那么在circle里快的
# 总会追上慢的。所以我们让慢的速度为1，快的速度为2，如果快的最终到达的linkedlist的end也没有追上慢的的话
# 那说明没有circle，如果中间有一时刻fast追上slow了，也就是fast==slow的话，就说明有circle，return True

# 这个方法首先是inplace的不需要extra memory
# 这个方法的runtime是这样的，我们要分类讨论:

# 对于没circle的linkedlist而言，fast到终点了就结束，时间肯定是O(n)

# 对于有circle的linkedlist而言，我们可以把它分成non-cyclic part和cyclic part
# （如果整个linkedlist就是一个大circle那non-cyclic part长度就是0）
# 假设整个linkedlist一共有n个 unique nodes，cyclic part有k个nodes，那么non-cyclic part就是n-k个nodes
# 如果我们看slow在开始到一直被fast追上的这个过程，在non-cyclic part，slow走n-k步
# 等它刚进入cyclic part的时候，fast当然已经在圈里了，这个时候的worst case就是fast 刚好到了slow紧后面
# node，那么因为fast和slow的速度差是1，一圈的长度是k，那么fast想要再扣圈追上slow的话，slow在fast追上
# 它之前还要走k-1步。因此slow在整个过程中一共走了n-k+k-1=n-1步 所以对于有circle的linkedlist而言
# 这个algorithm的time compleixity也是O(n)



class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        fast=slow=head
        #注意用快慢指针的时候，while loop都得这么写，while fast and fast.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return False