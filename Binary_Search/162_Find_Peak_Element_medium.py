#如果input list全部都是由一个一个小山包组成，那么这个方法没啥太大的优势
#但是如果这个inputlist是一个个的大山，即uphill和downhill都是很长的一类递增或递减的数字的话，那么这个方法还是很有用的

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return
        #如果inputlist只有一个element，那它自己一定是peak了
        if len(nums)==1:
            return 0
        else:
            start=0
            end=len(nums)-1
            while start<end:
                mid=start+(end-start)//2
                # 如果mid是小于它右边的邻居的，那说明mid在一个上坡上，peak一定在mid的右侧
                # 因为peak的右边的邻居就比peak大了，peak自己没有嫌疑，start=mid+1
                if nums[mid]<nums[mid+1]:
                    start=mid+1
                # 因为题中说了，一个element和它的下一个element是不可能相等的，因此else在这里
                # 只意为，mid大于mid+1对应的item。这说明mid在一个下坡上，peak可能就是mid也可能在mid左边
                # 我们不能排除mid的嫌疑。因此end=mid
                else:
                    end=mid
            #while loop terminate的时候一定是start和end重合时，可以验证重合时两个pointer指向的一定都是peak
            #真的有peak的就不说了，假设inputlist全部都是值递增的，那么我们要return的peak应该就是inputlist的最后
            #一个item（如果是递减的就要return第一个item。因为题中说可以assume这个inputarray的第一个的前面的item
            # 和最后一个的后面的item都是无限小的）。观察以后可以发现，start是会跑到最后去和end在end的初始位置重合的、
            # 因为就算是纯递增或纯递减也是有可以return的解的，所以不需要post processing
            return start