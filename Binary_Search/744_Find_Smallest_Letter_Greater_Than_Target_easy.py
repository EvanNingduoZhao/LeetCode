# 典型的binary search的题
#  但是要重点看最后为什么要return letters[start],要记住该怎么讲，把情况都分析全，才能impress面试官

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

letters=["a","b","d","e","f"]
print(nextGreatestLetter(letters,"c"))



