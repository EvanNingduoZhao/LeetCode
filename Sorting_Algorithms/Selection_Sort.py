# Selection sort的原理是，从list的第一项开始往后traverse，找到整个list里的min，把min和list的第一项
# 调换位置，那么现在第一项是sorted的了。继续从第二项开始往后traverse，找到从第二项到结尾这些elements
# 里面的min，再将这个min与第二项调换位置，那么现在前两项都是sorted的了。重复这个过程直到整个list都
# 被sorted。Selection sort是inplace的 time complexity是O(n^2)

#很短很清楚的一个视频 https://www.youtube.com/watch?v=g-PGLbMth_g&t=91s
input=[2,8,5,3,9,4,1]

def selection_sort(nums):
    if not nums:
        return None
    #用外面的for loop控制我们从list的那个element开始这次traversal
    #这时 current i的左边的所有elements都是已经被sorted的了
    #注意这里只要一直sort到倒数第二个element就够了，因为如果放在倒数第二个的位置
    #的是剩下的两个数里的min，那么剩下在list结尾的一定是整个list里最大的
    for i in range(len(nums)-1):
        minIndex=i
        #用inner for loop找到目前还没有被sorted的elements里的min的index
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minIndex]:
                minIndex=j
        #有可能我们刚刚完成的这次traversal的starting point就正好是还没有被sorted的elements里
        # 的min，那就不用swap了。否则我们swap nums[i]和nums[minIndex]
        if minIndex!=i:
            temp=nums[i]
            nums[i]=nums[minIndex]
            nums[minIndex]=temp
    return nums


if __name__ == "__main__":
    print(input)
    print(selection_sort(input))


