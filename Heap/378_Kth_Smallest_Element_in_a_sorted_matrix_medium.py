#这道题首先看到第k小或者第k大个element就要想到用heap
#那么问题是我们该以什么样的顺序把matrix里的elements给push到heap里去呢
#既然我们是要找第k小的，那么我们就把最小的先push进去，pop出来以后在把比他稍微大一些的push进去
#在这个过程中始终维持heap，这样第k次pop出来的value就是我们要的答案
#那么比他稍微大一点的该是什么的，应该是它右边的和它下面的，每次pop出去一个以后就把pop出去的那个element
#在matrix中的紧右侧和紧下侧的element push到heap里
#因为我们要知道每次被pop出来的element在matrix里的坐标，从而知道它下面的和右边的是什么，所以
#每次push进stack的时候我们push进去的是是一个tuple，tuple的第一个element是matrix里的值
        #tuple的第二个element是一个tuple，即那个值在matrix里的行列坐标

#同时我们还需要用一个set来记录所有被我们push进heap过的element在matrix里的坐标，这样不会重复
#push同一个element

#我们的目标是，第n次pop出来的element必须是matrix里第n小的，也就是目前在heap里没有被pop出来的
#和没进heap的所有element里目前最小的那一个是我们每次要pop出来的

# 为什么每次只需要push进去被pop出来的element的右边和下面的element是可以达到上面的要求的呢
#举例说明：
# 1  5  9
#10 11 13
#12 13 15

#这个matrix，我先push在pop出来1，再push进去5和10，pop出来5，在push进去9 和11
#这里是第一次需要做选择的地方，为什么值push 9和11？因为5pop出来以后我们下一步的目的是
#找到9 10 11 13 12 13 15这些element里最小的
#因此想10下面的element 12 就肯定没必要现在就被push到heap里去，因为我们要找的是剩下里最小的，
#而12这个位置的数一定比10大。而刚被pop出去的5的右面和下面的element 9和11有可能是剩下里的最小的
#当然11在这里同样也是10的右面的element，但在实际操作中这个algorithm是不知道11和10的位置关系的

#因此这个算法的核心思想是：既然我们每次都是要找剩下里的最小的，那么对于没被pop出去的element，他们
#下面的和右面的我们先不考虑，因为它们自己都没被pop出去，它们下面和右边的还比它们自己更大，更不可能了
#因此，每次pop出去一个element以后，我们再把它的下边和右边的elements push到heap里来
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #下面的这些用来实现heap的helper functions和heap implementation里的几乎一样
        #只不过这里因为每次push的heap里的是一个tuple，tuple的第一个element是matrix里的值
        #tuple的第二个element是一个tuple，即那个值在matrix里的行列坐标
        def __swap(heap, i, j):
            heap[i], heap[j] = heap[j], heap[i]

        def __floatUp(heap, index):
            parent = (index - 1) // 2
            if index == 0:
                return
            #所以在这里这些比较大小的地方要access value的值得用heap[index][0]才行
            if heap[index][0] < heap[parent][0]:
                __swap(heap, parent, index)
                __floatUp(heap, parent)

        def __bubbleDown(heap, index):
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < len(heap) and heap[left][0] < heap[largest][0]:
                largest = left
            if right < len(heap) and heap[right][0] < heap[largest][0]:
                largest = right
            if largest != index:
                __swap(heap, largest, index)
                __bubbleDown(heap, largest)

        def __push(heap, num, i, j):
            if len(heap) == 0:
                heap.append((num, (i, j)))
            else:
                heap.append((num, (i, j)))
                __floatUp(heap, len(heap) - 1)

        def __pop(heap):
            if len(heap) == 0:
                return
            elif len(heap) == 1:
                return heap.pop()
            else:
                __swap(heap, 0, len(heap) - 1)
                res, (i, j) = heap.pop()
                __bubbleDown(heap, 0)
                return res, (i, j)
        # Edge Case
        if not matrix or len(matrix) == 0:
            return None

        else:
            heap = [(matrix[0][0], (0, 0))]
            #用一个set来记录matrix里那些值是已经放到heap里的，那些是还没遇见过的
            visited = set()
            visited.add((0, 0))
            #用来控制while loop的执行次数，pop出来的第k个element就是要return的
            count = 0
            res = heap[0][0]
            while count < k:
                #因为heap里每一个element都是一个tuple，所以pop出来的也得两个element接着
                res, (i, j) = __pop(heap)
                #如果被pop出来的element在matrix里的下面的那个element没被push进heap过的话
                #就把它和它的行列坐标一起push到heap里，并且把它的行列坐标加到visited里
                if (i + 1, j) not in visited and i + 1 < len(matrix):
                    __push(heap, matrix[i + 1][j], i + 1, j)
                    visited.add((i + 1, j))
                # 如果被pop出来的element在matrix里的右面的那个element没被push进heap过的话
                # 就把它和它的行列坐标一起push到heap里，并且把它的行列坐标加到visited里
                if (i, j + 1) not in visited and j + 1 < len(matrix[0]):
                    __push(heap, matrix[i][j + 1], i, j + 1)
                    visited.add((i, j + 1))
                count += 1

            return res

##以下是不用自己implement heap，直接用python自带的heapq module来写的版本
#注意heapq里的heap是可以是list of tuples的，每一个heapnode的value必须在tuple的第一个element
#第二个element是啥无所谓，这道题里是element在matrix里的坐标
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or len(matrix)==0:
            return None
        else:
            heap=[(matrix[0][0],(0,0))]
            visited=set()
            visited.add((0,0))
            count=0
            res=heap[0][0]
            while count<k:
                res,(i,j)=heapq.heappop(heap)
                if (i+1,j) not in visited and i+1<len(matrix):
                    heapq.heappush(heap,(matrix[i+1][j],(i+1,j)))
                    visited.add((i+1,j))
                if (i,j+1) not in visited and j+1<len(matrix[0]):
                    heapq.heappush(heap,(matrix[i][j+1],(i,j+1)))
                    visited.add((i,j+1))
                count+=1
            return res
