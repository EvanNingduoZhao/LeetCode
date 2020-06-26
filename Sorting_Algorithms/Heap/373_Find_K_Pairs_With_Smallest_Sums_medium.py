#这道题的思路其实和378题是一摸一样的
#如果把nums1里的数竖着作为行的tile，nums2里的数横着作为列的title
#构建出一个table，table里的每一个值等于其所在位置的行上对应的nums1里的数和列上对应的nums2里的数之和
#那么这个table就是完全符合378题要求的table，直接用378题的方法就就好了
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if not nums1 or not nums2:
            return
        else:
            heap = [(nums1[0] + nums2[0], (0, 0))]
            res = []
            count = 0
            visited = set()
            visited.add((0, 0))
            while count < k:
                if heap:
                    new_sum, (i, j) = heapq.heappop(heap)
                else:
                    return res
                #因为要return的是所有前k小的sum的两个加数
                #因此每次pop出坐标了以后就在nums1和nums2里根据坐标找到对应的数，作为list
                # append到res里
                res.append([nums1[i], nums2[j]])
                if i + 1 < len(nums1) and (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    heapq.heappush(heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                if j + 1 < len(nums2) and (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    heapq.heappush(heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                count += 1
            return res