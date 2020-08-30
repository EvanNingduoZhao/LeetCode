#方法1 先sort nums，之后用two pointers
#因为2sum take O(N),那么3sum加了一个dimension，应该take O(n^2),但sort只take O(nlogn)
#所以sort一下nums不影响最后的time complexity
#我们的基本思路是要在这个sorted list里用for loop一个一个过
#假设新碰到的item叫A，那么我们就用two pointers在sorted nums的A的右边的部分找和等于A的complement的pair
#每次two pointers take O(n)一共来n次所以是O(n^2)

#下面code里的comment重点写了怎么避免duplicate的策略
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)<3:
            return None
        else:
            nums.sort()
            res=[]
            for i in range(len(nums)):
                #因为我们先sort了，所以如果我们碰到了一个正的元素，那它后面的元素
                #肯定是比他还大的正的
                if nums[i]>0:
                    break
                #如果nums[i]==nums[i-1]即和sorted nums里的前一个item相等，那我们直接跳过它
                #因为我们之前已经用two pointers找过这个值的complement的pairs了
                if i==0 or nums[i]!=nums[i-1]:
                    target=0-nums[i]
                    l=i+1
                    r=len(nums)-1
                    while l<r:
                        if nums[l]+nums[r]==target:
                            res.append([nums[i],nums[l],nums[r]])
                            #找到一个合格的pair以后要同时移动l和r两个pointers
                            l+=1
                            r-=1
                            #注意对于[-2,0,0,2,2]这种input，我们在i指向-2时找到了nums[1]的0和nums[-1]
                            #的2作为一个pair相加等于2，那么我们同时move了l和r之后l和r还是指向0和2，
                            #这个时候再把这一对也加到res里就有duplicate了，在找到一个pair并同时移动了
                            #l和r以后，要check移动过后的l和移动前的l指向的是不是值相同的item
                            # 这里不需要check移动前后的r所指向的item的值是不是相同，因为移动后的r
                            #指向的元素一定是<=移动前r指向的元素的，所以l如果移动后还和移动前指的item的值一样
                            #那么nums[l]+nums[r]一定是小于等于target的，小于得l+=1,这是这个technique的
                            #根本思想，等于也得l+=1，因为这说明现在发现的这个pair和之前发现的那个pair是
                            #duplicate
                            while l<r and nums[l]==nums[l-1]:
                                l+=1
                        elif nums[l]+nums[r]<target:
                            l+=1
                        else:
                            r-=1
            return res

# 这道题的第二种解法是在主体结构不变的情况下用把two pointers technique换成hashSet
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)<3:
            return None
        else:
            nums.sort()
            res=[]
            for i in range(len(nums)):
                #因为我们先sort里，所以如果我们碰到了一个正的元素，那它后面的元素
                #肯定是比他还大的正的
                if nums[i]>0:
                    break
                if i==0 or nums[i]!=nums[i-1]:
                    pairSum=0-nums[i]
                    j=i+1
                    # 注意 这里我们要给每一个i都重新搞一个hashset，原因如下
                    # 比如说nums被sorted过后是[-3,-2,-1,0,1,2,2,3,5]
                    # 那么在i是-2时我们建了一个hashset，里面有-1 0 1 2 3 5
                    # 对于-2 我们可以用这个hashset里的任一元素来组建三个数的组合
                    # 但是当i=-1时我们只能用0，1，2，3，5了，-1不能用了，
                    # 但是我们如果不用一个新的hashset的话，-1还是在hashset里的
                    # 所以为了排除掉不应该在hashset里的元素，对于每个i我们都要搞一个新的hashset
                    # 这其实和two pointers里l pointer从i+1开始是一个道理
                    # 我们把这个问题起名为确定一个item以后combination of three里的另外两个只能
                    # 用它右边的items问题
                    seen=set()
                    while j<len(nums):
                        complement=pairSum-nums[j]
                        if complement in seen:
                            res.append([nums[i],nums[j],complement])
                            while j+1<len(nums) and nums[j]==nums[j+1]:
                                j+=1
                        seen.add(nums[j])
                        j+=1
            return res

#这道题如果不能modify 或者copy input的话，那就不能sort了
#就没法用two pointers了，因为two pointers的前提是input是sorted
#解决的办法如下：用dup这个hashset()来记录我们在外层for loop traverse的过程中
#之前有没有遇到过跟这个item的value相同的item
#之后用seen这个dict来解决上面所说的 "确定一个item以后combination of three里的另外两个只能用它右边的items问题"
#具体怎么用的看code里的comment
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return None
        else:
            res = set()
            dup = set()
            seen = {}

            for i, val1 in enumerate(nums):
                if val1 not in dup:
                    dup.add(val1)
                    for j, val2 in enumerate(nums[i + 1:]):
                        complement = 0 - val1 - val2
                        #这里complement在seen里不够，还必须是seen里以complement作为key的那个pair
                        #的value是i，因为只有符合这个条件我们在知道这个complement是在我们目前
                        #外层for loop所在的那个item的右边
                        if complement in seen and seen[complement] == i:
                            res.add([val1, val2, complement].sort())
                        #即我们用内层for loop每遍历一个item，我们就在seen里把key是这个item的值的pair
                        #的value设成i，这样我们就知道，我们在外层for loop到目前的val1这个item时的这个
                        # iteration里，我们已经碰到val2这个item了，也就是说（在外层for loop的这个
                        # iteration里）之后可以用它来作为complement
                        seen[val2] = i
            return res
