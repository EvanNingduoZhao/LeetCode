input=[2,8,5,3,9,4,1]

def merge_sort(nums):

    #这里merge是一个helper function，merge_sort的主要内容在下面

    # 把两个sorted的list merge在一起，实际上是一个两个阵营的擂台赛
    def merge(nums1, nums2):
        res = []
        #c1和c2是记录两个nums1 和nums2两个list分别是哪个选手正在擂台上比赛
        c1 = 0
        c2 = 0
        #两个sort好的nums1 nums2进来，先比较两个list各子的第一个element比大小
        #小的那个被append到要return的res上，大的作为擂主和另一个阵营的下一个element继续比
        #依旧是小的被append到res上
        while c1 < len(nums1) and c2 < len(nums2):
            if nums1[c1] > nums2[c2]:
                res.append(nums2[c2])
                c2 += 1
            else:
                res.append(nums1[c1])
                c1 += 1
        #如果是nums1的所有选手先都输光了，都被push到res里了
        if c1 == len(nums1):
            #那就把nums2里剩下还没上过场的都挨个append到res里
            while c2 < len(nums2):
                res.append(nums2[c2])
                c2 += 1
        #如果是nums2的所有选手先都输光了也同理
        else:
            while c1 < len(nums1):
                res.append(nums1[c1])
                c1 += 1
        return res



    #base case，只有一个element的list一定是已经sorted的
    if len(nums)==1:
        return nums
    else:
        #首先从中间把nums分成两半
        mid=len(nums)//2
        left=merge_sort(nums[:mid])
        right=merge_sort(nums[mid:])
        #左右两半分别sort好以后把两半merge起来之后return，具体怎么merge的看上面helper function
        result=merge(left,right)
        return result


if __name__ == "__main__":
    print(input)
    print(merge_sort(input))

