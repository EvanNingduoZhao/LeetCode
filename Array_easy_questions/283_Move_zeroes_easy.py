# slow and fast two pointer technique,slow pointer records that before which element, all non-zero element are already
# dealt with and put into correct position. Then once the fast pointer finds another non-zero element, we place it
# at the position that the slow pointer is currently pointing to. Once the fast pointer iterates through the whole array,
# we set all element after the slow pointer's current position in the array to zero.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            nums = nums
        else:
            i = 0
            for num in nums:
                if num != 0:
                    nums[i] = num
                    i += 1
            for k in range(i, len(nums)):
                nums[k] = 0
