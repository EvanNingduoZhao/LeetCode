
class Solution:
    def findUnsortedSubarray(nums):
        if len(nums)<2:
            return 0
        else:
            min,max=None,None
            left=1
            right=len(nums)-2
            #先通过一个for loop找到第一个前一个比后一个小的地方（unsorted subarray开始的地方）
            for k in range(1,len(nums)):
                if nums[k]<nums[k-1]:
                    min = nums[k]
                    left = k
                    break
                #如果array iterate到头了还没有发现这样的开始点，那说明整个array的顺序都是对的 直接return 0
                if nums[k]>=nums[k-1] and k == len(nums)-1:
                    return 0

            #从开始点往后找，找到最小值，因为如果开始点后面有比开始点前面的值还小的值的话，那就意味这开始点要挪到前面那个值
            # 只有这样subarray sort以后才能得到正序的完整array
            while left<len(nums):
                if nums[left]<min:
                    min=nums[left]
                left+=1

            #之前是从前往后找开始点，现在从后往前找结束点，一样的思路
            for j in range(len(nums)-2,-1,-1):
                if nums[j]>nums[j+1]:
                    max = nums[j]
                    right = j
                    break
                if nums[j]<=nums[j+1] and j==0:
                    return 0
            while right>-1:
                if nums[right]>max:
                    max=nums[right]
                right-=1


            #最后确定开始点和结束点要挪到20行里说的"哪个值"
            start=0
            end=0
            for i in range(0,len(nums)):
                if nums[i]>min:
                    start=i
                    break
            for n in range(len(nums)-1,-1,-1):
                if nums[n]<max:
                    end=n
                    break
            #注意最后的长度要+1
            return end-start+1

    test = [1,2,3,3,3]
    print(findUnsortedSubarray(test))

        # if len(nums)==1:
        #     return 0
        # else:
        #     ans=0
        #     max=nums[0]
        #     k = 1
        #     while nums[k] > nums[k - 1]:
        #         if k == len(nums) - 1:
        #             return 0
        #         max = nums[k]
        #         k += 1
        #     start_index = k - 1
        #     start_value = nums[k - 1]
        #     print("start_value is "+str(start_value)+" and start_index is "+str(start_index))
        #     for i in range(k, len(nums)):
        #         if nums[i]>=max:
        #             max=nums[i]
        #             print("max is "+str(max))
        #         else:
        #             if max == start_value:
        #                 if start_index == 0:
        #                     ans = i - start_index + 1
        #                     start_index=-1
        #                 else:
        #                     j = start_index - 1
        #                     while nums[i] < nums[j]:
        #                         j -= 1
        #                     ans = i - j
        #                     start_index = j
        #                     start_value = nums[j]
        #                     print("while #start_value is " + str(start_value) + " and start_index is " + str(start_index))
        #             else:
        #                 if nums[i]>=start_value:
        #                     print("if #nums[i] is "+ str(nums[i])+" and start value is "+str(start_value))
        #                     print("if #i is "+str(i)+"  and start index is "+ str(start_index))
        #                     ans=i-start_index
        #                     print("if # ans is "+str(ans))
        #                 else:
        #                     print("else #nums[i] is " + str(nums[i]) + " and start value is " + str(start_value))
        #                     print("else #i is " + str(i) + "  and start index is " + str(start_index))
        #                     j=start_index-1
        #                     while nums[i]<nums[j]:
        #                         j-=1
        #                     print("j is "+str(j))
        #                     ans=i-j
        #                     print("else # ans is " + str(ans))
        #                     start_index=j
        #                     start_value=nums[j]
        #     return ans

    # if len(nums) == 1:
    #     return 0
    # else:
    #     ans = 0
    #     max = nums[0]
    #     k = 1
    #     while nums[k] > nums[k - 1]:
    #         if k == len(nums) - 1:
    #             return 0
    #         max = nums[k]
    #         k += 1
    #     start_index = k - 1
    #     start_value = nums[k - 1]
    #     for i in range(k, len(nums)):
    #         if nums[i] >= max:
    #             max = nums[i]
    #         else:
    #             if max == start_value:
    #                 if start_index == 0:
    #                     ans = i - start_index + 1
    #                 else:
    #                     j = start_index - 1
    #                     while nums[i] < nums[j]:
    #                         j -= 1
    #                     ans = i - j
    #                     start_index = j
    #                     start_value = nums[j]
    #             else:
    #                 if nums[i] >= start_value:
    #                     if start_index == 0:
    #                         ans = i - start_index + 1
    #                     ans = i - start_index
    #                 else:
    #                     j = start_index - 1
    #                     while nums[i] < nums[j]:
    #                         j -= 1
    #                     ans = i - j
    #                     start_index = j
    #                     start_value = nums[j]
    #     return ans