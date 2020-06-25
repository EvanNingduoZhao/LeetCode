# Insertion sort 的原理和扑克牌顺牌是一个道理，从一个list的第二个element开始，把这个element insert
# 到它左边的合适的地方。但是用code实现的方法跟扑克牌顺牌不一样，code没法直接找到那个合适的位置之后把牌
# 插进去。code的实现中，我们对于目前traverse到的这个element A，我们让他依次跟它前面的一个element相比
# 如果目前的这个element比它前面的那个element还小的话，就swap它俩，直到A被swap到一个它比它前面的那个
# element大的位置 Inserttion sort也是in place， time complexity也是O(n^2)

# insertion sort和bubble sort的区别：
# bubble sort（没有flag）不管input的list是什么order take的time都是一样的

input=[2,8,5,3,9,4,1]

def insertion_sort(nums):
    for i in range(1,len(nums)):
        j=i
        while j>0 and nums[j]<nums[j-1]:
            temp=nums[j-1]
            nums[j-1]=nums[j]
            nums[j]=temp
            j-=1
    return nums

if __name__ == "__main__":
    print(input)
    print(insertion_sort(input))