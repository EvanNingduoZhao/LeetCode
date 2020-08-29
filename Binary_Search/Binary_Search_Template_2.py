
class Solution:
    # 在模版1的comments里说了模版1和2在while loop的结束条件，以及return的条件和方式的不同
    #这里就说一下为什么模版2结束时，start和end同时指向的那个item一定就是我们要找的那个
    #（前提是input里保证有要return的item）
    # 因为我们在调整start和end的位置时，永远都是保证以他俩作为左右boundary pointers的这个inclusive的range
    # 是一个嫌疑range，即在这个range里的item一定都是有嫌疑成为我们最后该return的item的元素
    # 没有嫌疑的不配进来，有嫌疑的一个都不能放过
    # 那么当start和end重合时，这个嫌疑range里就只有一个元素了。这个时候分两种情况
    # 如果这道题是肯定保证input里是有我们该return的那个item的话，那么保证有一个罪犯，又只有一个人有嫌疑
    # 那这个人一定就是罪犯，第二种情况是如果input不保证一定有要return的那个item的话，那就是不一定有罪犯，
    # 但是有一个有嫌疑的人，所以最后return之前我们还要做一个post processing，来看看这个有嫌疑的人是不是真的
    # 是罪犯。如果是就return这个item。

    #这个模版里写的code解决的问题是，找到一组从小到大sorted的数字里，比target大的数里最小的那个数
    def binary_search_template_2(nums,target):
        # 这里的if里的内容只是place holder，代表的时候最开始如果需要的话，要用if来cover一些极端的情况
        # 不要看这个if具体内容
        if target >= nums[-1]:
            return nums[0]
        else:
            #模版2正式开始
            start = 0
            end = len(nums) - 1
            # 模版2的第一个特点就是while后面的condition是小于
            while start < end:
                # mid的计算这样写的效果是和(start+end)//2的效果一样的
                # 但是(start+end)//2只适用于python而这个写法适用于所有语言
                mid = start + (end - start) // 2
                # mid就是没嫌疑，把mid从range里排除，start=mid+1
                # 这个if后面的条件也是一个place holder，代表的情况就是
                # mid左边包括mid自己都没有嫌疑，从此我们只研究mid右侧的部分
                if nums[mid] <= target:
                    start = mid + 1
                # mid有嫌疑，mid保留在range里，end=mid
                else:
                    end = mid
                # 以上的这个if else解决的是要判断mid是不是要return的item还需要看mid的左边邻居的问题
                # （这个问题里之所以看左边邻居是因为mid比target大的前提下，mid左边的邻居必须比target
                # 小的情况下，mid才是比target大的数里最小的）
                # 如果问题改成要找比target小的里最大的，那需要看的就是右边的邻居了，那么start和end的调整
                # 也要改成start=mid，end=mid-1，来保证嫌疑range里全都是有嫌疑的且包含所有有嫌疑的
            #如果不需要进行post-processing，就这样写，直接return start就好了
            return nums[start]

            #如果需要post-processing，就写：
            if nums[start] 符合要被return的item的条件：
                return nums[start]
            else:
                return None 或者 -1
