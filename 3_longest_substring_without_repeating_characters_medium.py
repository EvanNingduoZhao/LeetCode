class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # first we cover the base case
        if not s or len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            # since if take a linear approach, this problem obviouly involves checking if we have already gone through a specific character, we apply a hashtable data structure
            dict = {}
            # 从start开始往下走，每碰到一个新char就char作为key，char的index作为value存到hashtable里，并计算从start到目前char的距离，和已知最大长度比较得出现最大长度。如果碰到的是已经见到过的char：
            # 1.如果上次见到该char是在目前的start之前，那么不影响，还是计算距离，比较，得出现最大长度
            # 2.如果上次见到该char是目前的start之后，那么只有把start变成上次这个char出现的紧接着后一个index，i才能继续往下走得到non repeating substring
            # 想明白为什么出现情况2时，任何一个原start和新start之间的char作为start都不能构造出更长的non repeating substring
            start = maxlength = 0
            for i in range(len(s)):
                if s[i] in dict and start <= dict[s[i]]:
                    start = dict[s[i]] + 1
                else:
                    maxlength = max(maxlength, i - start + 1)
                dict[s[i]] = i
            return maxlength

# 自己写的solution
# 比上述solution差在：
# 没有想到这一点：想明白为什么出现情况2时，任何一个原start和新start之间的char作为start都不能构造出更长的non repeating substring
# 自己的方法相当于同时兼顾好几个start，碰到已经见过的以后还再用一个forloop去把以每个start为开始的substring的长度都+1，自然效率比上述低。要理清逻辑，每次只跟踪单一最优start，想清楚什么情况下已经穷尽以本start开头的所有substring，什么时候该换start，在每一个阶段都采用直接计算出最优解的手段，而不是同时track好几个potential最优解
# my solution O(square of n)
#         if not s or len(s)==0:
#             return 0
#         elif len(s)==1:
#             return 1
#         else:
#             dict={}
#             length=[0]*(len(s))
#             keeper=0
#             max=0
#             for i in range(len(s)):


#                 if s[i] not in dict:
#                     dict[s[i]]= i

#                     for k in range(keeper,i+1):
#                         length[k]=length[k]+1
#                         if length[k]>max:
#                             max=length[k]


#                 else:

#                     candidates_keeper=dict[s[i]]+1
#                     if candidates_keeper>keeper:
#                         keeper=candidates_keeper
#                     dict[s[i]] = i
#                     for j in range(keeper,i+1):
#                         length[j]=length[j]+1
#                         if length[j]>max:
#                             max=length[j]
#             return max