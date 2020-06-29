#这道题是用heap的方法做的
#如果用quick select的话会更快，等学了quick select以后再做一遍

#先用一个dict把每个数字在nums里出现了多少次计算一遍，这个过程take O（n）
#在用heap求出来dict里value的前k名
#这里要注意以下几点：
#1.求一堆数里的最大的k个其实应该用minHeap是最高效的，因为用minheap的话，可以先一股脑push进去
# k个elements，之后heap里就维持着k个数量的element，每次见到一个新的，先push到heap里，在从heap
# 里把目前最小的那一个pop出来，这样每次进去一个新的都用新的来替换原来heap里的最小的，
# 在traverse完所有的数以后，heap里剩下的就是这一堆数里最大的k个了
# 用minheap的话，heap里一直都只有k个element所以push和pop的时间都是logk，一共pop和push
# 共进行n次，因此总时间是2nlog(k),题目中要求算法的时间复杂度必须优于nlogn，那么只有k=n时
#我们这个算法才是nlogn，但是对于k=n时，那说明nums里每个数只出现一次，我们直接return nums就
#好了，因此k=n是我们只take O(1)

#相反如果用maxheap的话，整个在traverse所有数的过程中，只能往heap里push，不能pop，
#最后把heap里的前k个pop出来,这种算法的时间复杂度是O(log1+log2+...+logn)=O(nlogn)是不如用
# minheap的

#2.用minheap的时候要注意，在heap里有了k个element以后，见到新的元素要先push再pop，不能先
# pop再push，否则如果新遇到的实际上比现在heap里有的都小的话，那先pop了heap里目前最小的就错了
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        else:
            count={}
            for num in nums:
                if num not in count:
                    count[num]=1
                else:
                    count[num]+=1
            heap=[]
            counter=0
            for key,v in count.items():
                #先一股脑push k个进去
                if counter<k:
                    heapq.heappush(heap,(v,key))
                    counter+=1
                #之后遇到新的先push再pop
                else:
                    heapq.heappush(heap,(v,key))
                    heapq.heappop(heap)
            res=[]
            for v,key in heap:
                res.append(key)
            return res

#第二种办法 用quick select
import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #首先还是用一个叫count的dict把每个数字在nums里出现了多少次给记下来
        if not nums:
            return None
        if k == len(nums):
            return nums
        else:
            count = {}
            for num in nums:
                if num not in count:
                    count[num] = 1
                else:
                    count[num] += 1
            #把nums里所有出现过的数字挨个不重复地存到unique这个list里
            unique = []
            for key, value in count.items():
                unique.append(key)

        #随机选择pivot index
        def __get_pivot_index(low, high):
            return random.randint(low, high)

        def __swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        #这里有一个重要的点
        def __partition(nums, low, high):
            # pivot_index是指unique里的element的index
            pivot_index = __get_pivot_index(low, high)
            # 但是具体这个pivot index指向的在unique里的这个数字具体在nums里出现了多少次
            # 得到count这个dict里去找，pivot_value指的就是出现了多少次
            pivot_value = count[unique[pivot_index]]
            # 我们要sort的还是unique，因为最后return的出现次数最多的那个数，而不是它们出现的次数
            # 但是我们sort unqiue不是根据unique里的element的大小来sort
            # 而是根据unique里的element在count里被记录出现的次数来sort它们

            #这里我们先把pivot element放到unique的开头
            __swap(unique, low, pivot_index)
            border = low
            for j in range(low, high + 1):
                # 到count里找j在unique里指向的那个元素在nums里出现了几次
                j_count = count[unique[j]]
                #因为我们要找前k多次数的，所以要降序排列的sort unqiue
                # 降序排列，大于pivot的在左边，小于pivot在右边
                # 所以这里用的是大于号
                if j_count > pivot_value:
                    border += 1
                    __swap(unique, j, border)
            __swap(unique, low, border)
            return border

        #这道题问的还和quick_select_implementation里写的不太一样
        #quick_select_implementation要的是第k个，就那一个
        #这道题里要的是前k frequent的，一共要k个，但是注意题里说，只要把这个k个return回来就行
        #在return回来的这个list里，这k个不用按顺序排列，因此这道题还可以用quick select
        #如果要求按顺序排列就只能用heap了

        #为什么这道题能用quick select：（这个例子里我写错了，按照正序sort写了，实际应该是从大到小sort）

        # 假设这道题要前5 frequent的，第一次partition把pivot放到正确的位置后，pivot的index是8(第九个)
        # pivot element A的值是10，那么也就是说现在在unique里在pivot element左边的这8个element都是小于
        # 10的，但是它们不一定是按顺序排列的。因此前5 frequent的数字一定都在这8个里，我们接下来只partition
        # unique在pivot element左边的部分。假设第二次partition把第二个pivot放到正确位置后，第二个pivot B
        # 的index是2（第3个），pivot element的值是4，那么现在在pivot B左边有2个数字，它们一定都是小于4的
        # 刚才我们第二次partition的unqiue的这个部分一共有8个元素，pivot B自己是一个，它左边2个，那它右边
        # 就还有5个，这5个一定都是大于4小于10的。我们接下来第三次partition，这次partition的是B右边这5个
        # 假设我们这次pivot index正好就是4（unique里的第五个），
        # 前面有四个加它自己正好五个，那么这五个一定就是unqiue里出现次数最多的5个。
        # 为什么？因为第三次partition虽然只partition 5个elements，pivot在unique里的index是4的话说明
        # 它左边有4个element，这4个里有1个是在第三次partition里被找出来的大于B但是小于第三个pivot C的，
        # 并且被扔到第三个pivot左边的一个element【管他叫M】，剩下三个里：2个是B左边的，有一个是B（
        # 第三次partition是不碰它们仨的，这三个一定都是小于等于B的，而我们第三次partition的都是B右边的，所以
        # 它们三个 包括M，一定都是小于pivot C的，也只有它们4个小于pivot C，因此pivot C加上它左边的4个就是我们
        # 要的结果）

        #以上就是为什么就算最后找出来的index等于k-1的那个pivot是在unique中间的一段（不把着开头结尾的）
        #里partition出来的，但是我们也可以保证，它加上它左边的就是我们要找的前k个

        # 1 2 4 5 7 8 8 9 10
        #     B M C        A
        def __quick_select(nums, low, high, k):
            pivot = __partition(nums, low, high)
            if pivot == k - 1:
                return
            elif pivot < k - 1:
                __quick_select(nums, pivot + 1, high, k)
            else:
                __quick_select(nums, low, pivot - 1, k)

        __quick_select(unique, 0, len(unique) - 1, k)
        return unique[:k]