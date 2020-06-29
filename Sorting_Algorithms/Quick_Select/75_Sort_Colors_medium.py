# quick select不是一般用来求第k个或者前k个（在不要求前k个也按顺序return的前提下）
# 那这道题是要把整个inputlist都排序，为什么还可以用quickselect呢

#因为这道题的特点是，input list里一共只有三种不同的数字，0，1和2
#因此以1作为pivot，做一个兼容duplicate的partitioning，结果就是所有的0都在1左边，所有的2都在1右边
#这其实就完成了sort了。

#具体这个兼容duplicate的partitioning改怎么做？ 还是和普通的quick select的partitionning有一定区别的
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def __swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        #这里我们用三个pointers，有两个zeros和twos分别从inputlist的开头和结尾开始
        #第三个pointer j用来traverse整个list
        #j碰到一个element等于0就扔到前面去，碰到2就扔到后面去
        #而zeros就一直指向最后一个被扔到前面的0（最右边的0），twos指向最后一个被扔到后面的2（最左边的2）
        def __partiton(nums):
            zeros = -1
            twos = len(nums)
            j = 0
            while j < twos:
                #j碰到0时
                if nums[j] == 0:
                    #先increment zeros让它指向list中第一个不是0的
                    zeros += 1
                    __swap(nums, zeros, j)
                    #注意这里只有把j碰到的0扔到前面去的时候，才继续increment j
                    #下面把j碰到的2扔到后面去的时候是不用increment j的
                    #因为这样可以保证，每次在increment border以后，border指向的那个第一个不是0的
                    #element一定是1，这样每次j遇到0，和border指向的1 swap的时候就把0 放到了list的前面
                    #把1放到了list中间，这是符合我们的目的的。
                    #为什么能保证border increment以后指向的一定是1呢，首先夹在border和j之间的element
                    #要不然是本身就是1，在j traverse时被跳过了，要不然就是j遇到了2，把2swap到后面时被swap
                    #过来的一个值 A，这个值可能是0 1 2，但是因为把2 swap到后面以后j 不increment，下一次
                    #while loop里j还是指向这个值，如果A是1，j跳过它，如果是0，会被swap到前面去，如果是2会被
                    #swap到后面去。总之就是被swap过来的这个A是0或者2，在下一次while loop里它还是会被弄走
                    #之后A是1的时候它才能留下来。当然，border和j之间的值也又可能是j把发现的0 swap到前面
                    #时被swap过来的一个值B，但是因为border 被increment以后只会碰到1，所以B一定是1
                    j += 1
                elif nums[j] == 2:
                    #j遇到2的话 swap以后不increment j，下一次whileloop
                    #j继续examine被swap过来的那个值
                    twos -= 1
                    __swap(nums, twos, j)
                #j遇到1就跳过
                else:
                    j += 1

        __partiton(nums)
        return nums