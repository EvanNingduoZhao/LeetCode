#这道题可以用三个指针，index1从nums1最后一个实际有效值开始，index2从nums2最后一个值开始，
# i从m+n-1开始，i是用来遍历keep track of现在比出来的值更大的放哪

#这里我们用的是merge sort里merge那个部分的擂主思想
#但是因为nums1是后面的部分空出来的，所以我们要从尾到头遍历，在m+n-1这个位置放nums1和nums2中最大的值
#之后进行擂台赛，更小的那个当擂主一直在台上和另一方的选手比，更大的被放到nums1里


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            # when modifying a input object within a function, 直接写nums1=nums2会让nums1指向一个
            # 新的memory slot，要想做到inplace modification需要element wise modify nums1
            nums1[:] = nums2

        index1 = m - 1
        index2 = n - 1
        i = m + n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] >= nums2[index2]:
                nums1[i] = nums1[index1]
                index1 -= 1
                i -= 1
            else:
                nums1[i] = nums2[index2]
                index2 -= 1
                i -= 1
        #最后如果是nums2先没了选手不用管，因为nums1剩下的选手就在nums1的开头
        #如果是nums1先没了选手，则把nums2里剩下的选手一个一个放到nums1里
        if index1 == -1:
            while index2 >= 0:
                nums1[i] = nums2[index2]
                i -= 1
                index2 -= 1
            return

nums1 = [0,0,0,0,0]
nums2 = [1,2,3,4,5]

merge(nums1,0,nums2,5)
print(nums1)
