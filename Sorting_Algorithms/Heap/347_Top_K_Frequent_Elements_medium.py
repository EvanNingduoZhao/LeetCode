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