#非常非常简单的一道题，注意这里用set就可以了 不需要dict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        else:
            record=set()
            for num in nums:
                if num in record:
                    return True
                else:
                    record.add(num)
            return False