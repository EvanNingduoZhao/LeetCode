#以下两种solution是这个问题的自己想的第一种思路，第一个solution是用dp list版的，第二个solution是只用4个variable版的
#这两个版本的时间复杂度差不多，但是第一个solution的空间复杂度是O(n)，第二个solution的空间复杂度则是O(1)

#再下面的是在discussion里看到的更简洁一些，但是同时也有些更难想的思路，但是可能DP题做多了以后可以发现这种思路反而
#适用更加广泛

#先说自己做题想出来的思路，这道题的sub problem就是，如果我决定rob一个house A，那么从A和所有在A左边的house里在符合
#no two adajecent houses的rule的前提下我一共可以最多rob多少钱，注意这个sub-problem的前提是A这个house我是必须rob的
#假设新house A在nums里的index是a，那么dp[a]这个位置就存着以nums[a]这个house为house A的subproblem的答案

#那么我们在沿着nums这个list traverse时，我每见到一个新的house时，以这个新house左边的每一个house为House A的sub-problem
#我都已经解决，并知道答案了。所以我是可以用新house左边的任何一个house作为house A的sub problem的答案来计算以
#新house作为house A的sub problem的答案的。那么怎么算的呢？假设我的nums是[4,2,7,9,3,1] 那么假设现在的新house是1
# 这个house的index是5
# 在有1块钱的这个house我一定要rob的前提下，那么我其实有两个选择，第一个是rob有9块钱的那个house（和新house隔1个house）
# 及它左边的符合规则可以rob的（所得总和就是nums[5]+dp[3]）。第二个是rob有7块钱的house（和新house隔两个house）
# 及它左边的符合规则可以rob的（所得总和就是nums[5]+dp[2]）。
# 有3块钱的不能rob因为不符合no two adjectent house rule。也不用考虑rob有两块钱的那个house（和新house隔3个house）
# 因为你只rob隔三个house的（nums里的2），但不rob隔一个house的（nums里的9），那就相当白给的9块钱你不要，这是不行的
# 换一种说法，隔三个house的house（2）其实是在考虑隔一个house的那个house（9）的左边的可以rob的house里就考虑过了
# 当然实际上跟考虑1作为新house一样，在rob 9的前提下也不一定非要rob 2，也可以rob 4

# 下面举一个例子，证明有的时候rob 隔两个house的house是可以更profittable的
# [2,20,9,3,1], 在这里，如果1是新遇到的house，那么rob隔一个的9和9左边可以rob的最多赚2+9+1=12
# 但是如果rob隔两个的20，和20左边可以rob的（这里没了）可以赚1+20=21

# 综上所述，假设新house A在nums里的index是a的话，那么dp[a]（即以nums[a]这个house为house A的sub problem的结果）
# = nums[a]+max(dp[a-2],dp[a-3])
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        elif len(nums)==3:
            return max(nums[0]+nums[2],nums[1])
        #因为这个方法涉及到要用dp[a-3]那么你想要-3就至少得有4个及以上的house
        #所以在nums的len小于等于3时都得作为base case来单独讨论
        else:
            dp=[0 for _ in range(len(nums))]
            dp[0]=nums[0]
            dp[1]=nums[1]
            dp[2]=nums[2]+nums[0]
            for i in range(3,len(nums)):
                dp[i]=max(dp[i-2],dp[i-3])+nums[i]
            # 最后的最高收益一定是最后一个或者倒数第二个house为house A的sub problem的结果
            # 不可能在倒数第三个，因为你要rob 倒数第三个的话，你就还可以rob最后一个
            return max(dp[-1],dp[-2])

# 上一个solution是用一个dp array来存所有的sub problem的答案的
#但是实际上，对于一个新的house我们需要的sub problem的答案只不过是a-3和a-2这两个house的
#当然也需要a-1，因为对于现在的新house是a-1的那个house，它对于现在新house的下一个house就是a-2了
#所以我们只需要用三个variable存dp[a-1],dp[a-2],dp[a-3]的值，之后再用一个current来存刚算出来的dp[a]就好了
#之后traverse每前进到一个新的house，就把这4个variabel都update一遍，这样一来相对于上面的solution要用一个
#占O(n) space的dp array而言，四个vairiable只占O(1) space.
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        elif len(nums)==3:
            return max(nums[0]+nums[2],nums[1])
        else:
            # 如果新遇到的house A的在nums里的index是a的话
            # 现在刚进入到else里默认的a是3，即第四个house
            # one_away代表的是以index是a-1那个house作为house A的subproblem的结果，即上个solution中的dp[a-1]
            one_away=nums[0]+nums[2]
            # two_away代表的是以index是a-2那个house作为house A的subproblem的结果，即上个solution中的dp[a-2]
            two_away=nums[1]
            # three _away代表的是以index是a-3那个house作为house A的subproblem的结果，即上个solution中的dp[a-3]
            three_away=nums[0]
            for i in range(3,len(nums)):
                current=nums[i]+max(two_away,three_away)
                three_away=two_away
                two_away=one_away
                one_away=current
            return max(one_away,two_away)

#discussion里的一个最高赞的思路，可以借鉴，按照这个方式去想可能遇到新的题能更快的找到思路
#对于一个house A来说，这个robber有两个选择，
# 第一rob这个house A，并且rob A的左边隔一个的house C，及所有符合
#no two adjecent house rule的C左边的house

# 第二不rob这个house A，rob A左边的house B，及所有符合
# #no two adjecent house rule的B左边的house

# 因此对于一个新见到的house A而言，假设它在nums里的index是a，那么在dp array，dp[a]里存的是
# 假设如果A是最后一个房子，那么这个robber在包括A在内的所有的房子里一共能robb多少钱
# （Note：这里是像上面的两个option说的那样，可以rob A也可以不rob A，哪个能抢更多钱就抢哪个）
# 这个思路的dp array里的值和上面自己的思路里时有本质区别的，上面自己的思路里dp[a]存的是
# 在assume必须rob A的前提下，再算上A左边的可以rob的，到A为止一共可以rob多少钱

# 综上在这个新思路中，dp[a]=max(dp[a-2]+nums[a],dp[a-1])
# 上面自己的思路了还cover了一个重要的问题，即可以选择rob A左边隔2个house的那个house，这个新思路
# 其实也是cover这个问题的，是这样work的：对于a而言，我可以选择rob a以及a-2 （a-2是a左边隔1个house）
# 但是对于dp[a-2]这个值而言，它可能是真的rob了a-2这个house的一个结果，也可能是没有rob a-2，而是
# rob了a-2-1即a-3这个house的结果。我们再说选择rob a以及a-2时，这里的rob a-2实际上也是两个option，
# 即上述的真的rob a-2，或者不rob a-2，实际上rob a-3。而a-3就是a的左边隔两个，所以新思路cover了这种选择

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            #prev1就是dp[a-1]
            prev1=0
            #prev2就是dp[a-2]
            prev2=0
            #a从第一个house开始，但因为这是prev1和prev2都是0
            #所以第一个current=nums[0]
            #当a=1时，prev1=nums[0],prev2=0,所以current实际上等于max(nums[1],nums[0])
            #到了a=2时，prev1和prev2都有值了，这个algortithm就开始像上面说的那样运行了
            for a in range(0,len(nums)):
                current=max(nums[a]+prev2,prev1)
                prev2=prev1
                prev1=current
            return max(prev2,prev1)