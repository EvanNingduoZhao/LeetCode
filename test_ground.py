
#
# # import heapq
# # maxHeap=[]
# # heapq.heappush(maxHeap,-1)
# # heapq.heappush(maxHeap,-2)
# # heapq.heappush(maxHeap,-3)
# # heapq.heappush(maxHeap,-4)
# # print(maxHeap)
# # print(heapq.heappop(maxHeap))
#
#
#
# l=[1,2]
# a=2
# print(l[a]==3)
# if a!=len(l) and l[a]==3:
#     print("yes")
# else:
#     print("No")
#
#
#
# def binarySearch(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     if len(nums) == 0:
#         return -1
#
#     left, right = 0, len(nums) - 1
#     # 模版1的特点一是while进行的condition是小于等于
#     # 特点一使模版1的return的条件和方式跟我们后面会见到的模版2有很大的不同
#     # 可以看到模版1(在不算post processing的前提下)，唯一的一个return
#     # 是在while loop里面，即每次进入了while loop里面以后计算出mid是多少
#     # 直接就check一下此时的mid是否符合target的条件，如果符合直接return
#     # 不管while loop有没有达到terminate的condition，algorithm直接结束，
#     # 而下面会见到的模版二的return的条件和方式则和模版1相反，模版2中，while
#     # loop进行的condition是小于且loop里面没有用来check mid是不是直接符合target的条件的步骤，只是根据
#     # mid的值来调整移动start和end （或者说left和right一回事），（同样不算
#     # post processing的前提下）模版2只会在while loop结束了以后才会return
#     # start，模版2的原理是while loop结束时start和end一定是指向同一个item的
#     # 只要input里是有target的，那最后start和end在while loop结束时指向的这个
#     # item就一定是是target，所以loop结束后return start（return end也一样因为两者是重合的）
#     while left <= right:
#         mid = (left + right) // 2
#         # 在while loop里面算出来了mid以后直接就check目前的mid是不是符合target的条件，如果符合直接return
#         if nums[mid] == target:
#             return mid
#         #因为之前check了mid符不符合target的条件，如果符合就已经return了，不会走到这了，因此
#         #只要走到这的mid一定都是没有嫌疑的，所以以下都是left=mid+1，right=mid-1这种把mid
#         #排除在外的调整
#         # target在mid右侧，mid没嫌疑
#         elif nums[mid] < target:
#             left = mid + 1
#         # target在mid左侧，mid没嫌疑
#         else:
#             right = mid - 1
#
#     # End Condition: left > right
#     # 这一步实际上是post processing，如果input中保证有我们要找的target的话
#     # 是不会碰到这一步的
#     return -1

print(int(2.9))
print(int(6//(-132)))

nums=[-1,-2,-3,0,1,5,6,7]
for i,val in enumerate(nums):
    print(i,val)


