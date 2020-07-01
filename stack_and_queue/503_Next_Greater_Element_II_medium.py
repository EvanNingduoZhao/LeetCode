#这道题和739题属于同一个类型题
#区别在于739题是只pass through input的list一次
#而这道题里我们的input list是循环的，理论上可以pass through无限次，但是实际上，pass through两次
#就够了 再多也没有用。因为pass through 第二遍就足以给在那些在自身不是nums最大的elements，但是
# 第一遍pass through时因为list中比它们大的元素都在它们之前
# 所以没有找到对应的下一个更大的element的elements
# 第二遍pass through就给了这些elements一个跟在自己之前的elements比较的机会

#所以只有值等于nums里的最大值的elements才会最后找不到对应的next greater element
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)==0:
            return None
        else:
            #stack stores the index in nums
            stack=[0]
            #先让所有elements对应的答案都等于-1
            #这样pass through nums两遍过后还是-1的就都就应该是-1
            #题中要求的是对于找不到对应的next greater element的element，return -1
            res=[-1]*len(nums)
            #pass through 第一遍，跟739题思路一样
            for i in range(1,len(nums)):
                while True:
                    if not stack:
                        stack.append(i)
                    else:
                        if nums[i]>nums[stack[-1]]:
                            res[stack[-1]]=nums[i]
                            stack.pop()
                        else:
                            stack.append(i)
                            break
            #pass through nums第二遍
            for i in range(0,len(nums)):
                while True:
                    if nums[i]>nums[stack[-1]]:
                        res[stack[-1]]=nums[i]
                        stack.pop()
                    #但是这次碰到比stack最后一个element对应的值
                    # 还小就不在append到stack上了，因为它们所对应的答案在第一遍pass的时候就找到了
                    else:
                        break
            return res