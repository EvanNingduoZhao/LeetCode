#这道题的第一种解法就是用heap sort来解，只不过是在extraction phase不用挨个都extract出来
#只需extract k次，第k个被extracted出来的的就是kth largest element
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #以下两个helper functions包括build heap的code都和Heap_Sort里的是一模一样的
        def __swap(heap, i, j):
            heap[i], heap[j] = heap[j], heap[i]

        def __bubbleDown(heap, size, index):
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left <= size - 1 and heap[largest] < heap[left]:
                largest = left
            if right <= size - 1 and heap[largest] < heap[right]:
                largest = right

            if largest != index:
                __swap(heap, index, largest)
                __bubbleDown(heap, size, largest)

        # build heap
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            __bubbleDown(nums, n, i)

        # Extraction phase
        result = nums[0]
        # 只extract k次
        for i in range(n - 1, n - k - 1, -1):
            __swap(nums, 0, i)
            result = nums[i]
            __bubbleDown(nums, i, 0)

        return result

#这道题看到答案里还有用quick sort相关的partition思想来解的
#学完quick sort以后再用那个方法做一下