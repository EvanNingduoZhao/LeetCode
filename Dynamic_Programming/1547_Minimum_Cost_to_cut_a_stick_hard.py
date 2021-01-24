# 这道题是这样的，我们用一个dp dict叫memo存信息，memo的key是一个tuple(i,j)，i和j代表一段sub stick的开始和结束的位置
# memo[(i,j)]存了把从i到j这一段rod该切的地方都切好需要的总cost
# 假设在开始于i结束于j的这段rod上我们第一刀切在i和j之间的k位置，那么memo[(i,j)]=memo[(i,k)]+memo[k,j]+(j-i),
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.memo={}
        # 我们定义一个recursive的helper function，用来计算cut开始于start，结束于end的rod的总cost
        def dp(start,end):
            #如果这一对start和end我们之前已经算过，那就直接return之前算好存起来的
            if (start,end) in self.memo:
                return self.memo[(start,end)]
            best=float('inf')
            # 如果题目给的cuts中没有cut的位置在start和end之间，那么我们在start和end之间不需要切
            # 那么cut 从start到end这段rod的cost就是0，cutInBetween就是我们用来记录start和end之间有没有cut
            # 的boolean flag
            cutInBetween=False
            # 我们把所有的cuts都过一遍，但是只关心在位置在start和end之间的
            for cut in cuts:
                if start<cut and cut<end:
                    cutInBetween=True
                    # 这start是目前的start，end是目前的end这层recursive call里，我们相当于
                    # 把start和end之间的每个cut point都作为cut从start到end这一段的第一刀试了一遍
                    # 那么每个不同的第一刀的位置，都会因为两个recusive call，分别是从start是start，end是第一刀的位置
                    # 和start是第一刀的位置，end是end。对于每个第一刀我们都会算出来一个dp(start,cut)+dp(cut,end)+end-start
                    # 我们拿它和目前的best比，不断update best。
                    best=min(best,dp(start,cut)+dp(cut,end)+end-start)
            # 如果for loop结束以后boolean flag还是false，那说明start和end之间不需要切，return 0
            if not cutInBetween:
                self.memo[(start,end)]=0
                return 0
            # 如果切了那就return best,并且把这一段的计算结果存到memo里
            self.memo[(start,end)]=best
            return best
        # 在主function里calldp(0,n)来触发这个top down的过程
        return dp(0,n)

# 这个解法space complexity是O（n平方）因为start和end最多可以有n平方种组合，worst case下它们每个都会在memo里
# time是O（n立方）因为对于每一对start和end都要过一遍所有的cut