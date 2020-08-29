# 典型的binary search的题
#  但是要重点看最后为什么要return letters[start],要记住该怎么讲，把情况都分析全，才能impress面试官

#以下是一个不符合模版的土办法，可以看一下土办法的分类讨论有多复杂，再对比下面的用模版2写的solution
#就可以发现模版2的solution有多么清楚了。
#土办法最大的问题是，while的condition是小于等于，那么就意味着在while loop结束时start和end是错开的
#即start 跑到end的右边去了。这就导致了很多复杂的分类讨论，其实想弄清楚这种方法下为什么直接return start就是对的
#也不用分类讨论那么复杂，可以这么想，用下面模版2里会介绍的嫌疑思维，即当mid>target时实际上mid也是有嫌疑的，因为
#我们要找的是比target大的里最小的，那么小于等于target的item肯定都是没嫌疑的，但是大于target的都是有嫌疑的（因为我们光看
# 这一个item不确定它是不是最小的那个比target大的）因此在mid比target大时让end=mid-1不是最好的，应该让end=mid
#end=mid-1就让mid这个本来有嫌疑的item暂时被排除了，如果该return的真的就是这个mid的话，
# 得等到最后start跟end错位了以后才能又start指向它。

#以上的comment是学完binary search复习时写的，以下在土办法代码里的comment是做题时写的，没有用嫌疑思维
#但是看一看也是有帮助的，可以很好的理解为什么土办法不好，模版2到底好在哪
def nextGreatestLetter(letters, target):
    #先考虑两个极端情况，因为letters的大小是wrap around的，即a比z大
    #所以如果target比letters的最后一个还大的话，就return letters的第一个
    if target>=letters[-1]:
        return letters[0]
    #如果letters的第一个就比target大的话，当然直接return letters的第一个
    if target<letters[0]:
        return letters[0]
    #下面开始用binary search
    else:
        start=0
        end=len(letters)-1
        while start<=end:
            mid=(start+end)//2
            print("mid is",mid)
            if letters[mid]==target:
                #因为考虑到可能有重复的letter在letters里
                #所以如果letters[mid]就等于target的话，我们要return的是letters中
                #下一个不等于，也就是比letters[mid]大的letter
                mid+=1
                while letters[mid]==target:
                    mid+=1
                return letters[mid]
            #这里是经典操作了
            elif letters[mid]>target:
                end=mid-1
            else:
                start=mid+1
        #这里最后为什么要return letters[start]其实是有学问的
        #这个问题的结束其实有两种结束情况，每种里又有两种小分支
        # 1.结束前end-start=2：
        # 假设一顿truncate以后剩下的是[a,c,e]，现在start=0指向a，end=2指向e，
        # 那么mid=1，指向c
        # 这里要分三种情况讨论了，
        # （1）如果target就等于c的话，那么程序会用inner的while loop找到
        # 下一个大于c的element之后return，这个情况非常简单，我们主要看后两种情况
        # （2）如果target等于d，即target是大于mid c的，那么start=mid+1就等于2，即和end一起
        # 同时指向e了，下一轮while loop的iteration里mid就等于start和end的平均，即start。
        # 那么现在mid是大于target了，end=mid-1，但是这时start是不动的，稳稳地指向最小的比target
        # 大的元素，安全return start
        #  （3）如果target等于b，那么target是小于mid c的，那么end=mid-1，即end和start一起
        # 同时指向a了，下一轮while loop的iteratiob里mid还是等于start和end的平均即start。
        # 那么现在mid是小于target的了，start=mid+1，即c即最小的比target大的元素，安全return start
        # 2. 结束前end-start=1：
        # 因为我们在计算mid=start和end的平均值时是舍掉所有小数部分的，因此在start和end只相差1时，
        # mid肯定等于start，还是有三种情况：
        # （1）这时假如剩下的是[a,b]，要找的target是c。start是a，end是b，那么mid也是a。
        # mid a小于c，那么start=mid+1，这时start=end=mid=b，再和target c比，还是小于c
        # start=mid+1 指向d（假设b的下一个是d），return d
        # （2）假如剩下的是[a,c],要找的是b，那么mid=start=a，mid小于b，start=mid+1=end=c
        # 这时mid=start=c，mid大于b，end=mid-1=a，start不动还是指向c，return start c，正确
        #  （3）假如剩下[b,c],要找的的target是a，那么mid=start=b，mid大于target a，end=mid-1，
        # start不动还指向b，return start b，正确

        #这一个小小的return start，其实背后有这么多分类讨论的问题，这里研究的是target大的里最小的
        #还有一种问法是找比target小的里最大的，这个是后就还是一摸一样的的code，只需要改两个地方
        # 第一是，在letters[mid]就等于target的时候要用while loop往前找，第二是最后要return end
        # 因为以上这6种情况，最后都是以start-end等于1结尾的，即start就是end紧后面的一个，那start
        #是比target大的里最小的，那target是夹在start和end中间的，那end就是小于target里最大的呗

        # 这种index的问题
        # 面试的时候现想肯定是难度很大的，所以要提前理解好，背好，练好。面试的时候直接现成的套路
        # 拿出来就用，


        return letters[start]

# 以下是标准的模版2solution，使用模版2最重要的就是嫌疑思维，即每次调整start和end时，只让有嫌疑的item
# 能够继续呆在从start到end inclusive的这个range里，不让没嫌疑的进来，同时也不能漏掉每一个有嫌疑的

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #首先考虑极端情况，因为像这道题一样，有的题目会有一些比较特殊的极端的条件
        #这些条件大多数是仅用binary search无法解决的，要用额外的if else来解决
        #比如这道题的letters also wrap around就是一个这种极端条件
        #我们在考虑极端条件时，可以多用点if else，把能想到的极端情况先都用if else给cover上
        #我们写完了整个algorithm以后可能会发现，有的极端情况的if else，不额外写上，只靠主体
        #的algorithm也是可以cover的，那就把它删掉就行了，这总比没考虑到这种情况要好
        if target >= letters[-1]:
            return letters[0]
        # 像下面这个被comment out的if就是一个预先写上的极端情况，结果写完主体代码发现其实这种
        # 情况下end会最后和start在start的初始位置重合，最后return start，光靠主体代码也可以cover
        # 所以就comment掉了
        # if target<letters[0]:
        #     return letters[0]
        else:
            start = 0
            end = len(letters) - 1
            #模版2的最大特点就是while后面的condition是小于
            while start < end:
                #这样写的效果是和(start+end)//2的效果一样的
                #但是(start+end)//2只适用于python而这个写法适用于所有语言
                mid = start + (end - start) // 2
                #mid小于等于target的话，mid就是没嫌疑的，因为我们要找的是大于target里最小的
                #因此把mid从range里排除，start=mid+1
                if letters[mid] <= target:
                    start = mid + 1
                #如果mid是大于target的话，那么mid是有嫌疑的，因此我们把mid保留在range里
                #让end=mid
                else:
                    end = mid
            #最后start和end重合时while loop结束，且两个pointer同时指向的那个element一定就是我们要找的
            #这里说一下为什么两个pointer同时指向的那个element一定就是我们要找的，因为
            #start和end最为左右boundary pointers的这个inclusive的range里，永远都只有有嫌疑是我们该return的那个
            #item的元素，那么当start和end重合时，这个range里就只有一个元素了。这个时候分两种情况
            #如果这道题是肯定保证input里是有我们该return的那个item的话，那么保证有一个罪犯，又只有一个人又嫌疑
            #那这个人一定就是罪犯，第二种情况是如果input不保证一定有要return的那个item的话，那就是不一定有罪犯，
            #但是有一个有嫌疑的人，所以最后return之前我们还要做一个post processing，来看看这个有嫌疑的人是不是真的
            #是罪犯。如果是就return这个item。
            return letters[start]




