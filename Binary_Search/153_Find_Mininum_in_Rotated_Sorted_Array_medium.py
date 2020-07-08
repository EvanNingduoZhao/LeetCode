class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        #如果nums的最后一个item是大于nums的第一个item的话，说明没有rotated
        #因为如果rotated了的话，应该是把原本比现在nums的最后一个item再大一点的那个item，及它后面所有
        #items都转移到nums的开头去，因此rotate了的话，nums的第一个item应该比nums的最后一个item大
        #因为题中说nums里是没有duplicates的，那么如果nums的最后一个item和nums的第一个item一边大的话，
        #说明nums只有一个item，因此只要nums[-1]>=nums[0]就return第一个item
        if nums[-1]>=nums[0]:
            return nums[0]
        start=0
        end=len(nums)-1
        while start<end:
            mid=start+(end-start)//2
            # 假设input是 4 5 6 7 2 3，我们可以发现，
            # 在min左边的item是一定比nums[0]和nums[-1]都大的
            # 在min右边的item包括min自己是一定比nums[0]和nums[-1]都小的
            # 那么只需要让mid和nums[0]比就行了，比nums[0]大说明min在mid右侧，mid自己排除嫌疑，start=mid+1
            # 如果mid比nums[0]小，那么mid有可能自己是min，也有可能min在mid左边，mid自己还是有嫌疑，end=mid
            # note：这里我们之所以用大于等于是因为，首先nums是没有duplicates，出现了nums[mid]=nums[0]
            # 的情况那一定是因为mid就等于0了，这种情况只会是因为end=1
            # start=0，end-start=1,mid=start=0这样产生的。假如nums是 7 2 3 4 5 6的话
            # 当end指向2，start指向7的时候，end和start只相差1，那这时mid就等于start等于nums[0]
            # 所以直接也start=mid+1，这下start就等于end了，直接return start
            # 上面说的一定是对的，因为如果nums是6 7 2 3 4 5的话，mid是永远不会等于nums[0]的，因为end移动到最左边
            # 也就是到2，这时start=6，那mid就等于7，之后start=mid+1=end就return start了，因此只要rotate过来的
            # item多于一个就不会产生mid=nums[0]的情况
            if nums[mid]>=nums[0]:
                start=mid+1
            #如果mid比nums[0]小
            else:
                end=mid
        # 这种写法就是结束的时候一定是start=end的
        return nums[start]
