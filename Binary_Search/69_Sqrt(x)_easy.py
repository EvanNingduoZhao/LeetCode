#这道题的input虽然不是一个list，但是我们可以把它当成在一个从0到x从小到大逐一增加的list里，
#找到一个平方等于x的item，这就是一个典型的binary search，且只看mid就可以确定这个mid是不是
class Solution:
    def mySqrt(self, x: int) -> int:
        #base case 如果x=0或者1的话直接return x就好了
        if x==0 or x==1:
            return x
        else:
            #开始binary search
            start=1
            #end=x-1为初始值，因为除了0和1以外再没有数字的平方根等于自己了
            end=x-1
            #这道题基本是属于，只需要看mid这一个element就知道target是在mid左边还是右边的
            #不完全属于，因为我们还是要确定mid+1的平方是要大于x的（原因见while loop里的第一个comment），
            # 即mid的平方和mid+1的平方能够把x夹在中间
            # 对于这样的mid我们直接return
            # 因此我们既可以使用模版1，也可以使用模版2：

            #这个class是模版1解法：while的条件是小于等于，while里面是要有if elif else的结构
            #一个if来check mid是不是符合直接return的标准，例如mid=target或者mid符合其他的要求的条件
            # （在这道题里这个return的条件是mid的平方和mid+1的平方能够把x夹在中间）
            #另外的elif和else用来take care of当mid不符合直接return的条件时，该移动start或者移动end
            # 的两种分类讨论情况
            while start<=end:
                mid = (start + end) // 2
                #因为这道题要把x真正的平方根的小数部分truncate掉,return的都是整数，例如x=15要return 3
                #因此只要mid的平方和mid+1的平方能把x夹在中间，就该return mid了
                if mid * mid <= x and x < (mid + 1) * (mid + 1):
                    return mid
                # 当mid的平方大于x时，mid自己没有嫌疑且target一定在mid的左侧方向，因此end=mid-1
                elif mid * mid > x:
                    end = mid - 1
                # 当mid的平方小于x且mid+1的平方不大于x时，mid自己没有嫌疑，且target一定在mid的右侧，因此
                # start=mid+1
                else:
                    start = mid + 1

#模版2解法：
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        else:
            start=1
            end=x-1
            while start<end:
                mid=start+(end-start)//2
                ms=mid*mid
                #这也不是标准的模版2，但是不check一下感觉可惜了
                if ms==x:
                    return mid
                elif ms>x:
                    end=mid-1
                else:
                    if end-start==1:
                        if end*end>x:
                            return start
                        else:
                            return end
                    start=mid
            return start