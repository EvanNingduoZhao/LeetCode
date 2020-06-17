#以下是这道题的从蛮力办法一步一步优化的过程，看一看这个过程可以很好的培养思路

#首先是蛮力办法：
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        #以每个num都作为起点，在list里搜索num+1在不在list里，如果在再搜索num+2在不在list里
        #直到num+n不在list里，记录下刚才一共找到了几个一连串的数
        for num in nums:
            current_num = num
            current_streak = 1
            #这里每次搜索current_num +1 是不是在nums里就要take O(n) time
            #对于一个长度是n的consecutive sequnce这样的搜索还要进行n次
            #而最外层的for loop要让num里的每一个element都做一次sequence的起点
            #所以总的time complexity是O(n^3)
            #但这个方法的优势是不需要extra space 完全是in place的
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

#第一步优化
#用空间换时间
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        # 用空间换时间，先用O(N)的时间和O（N）的空间 把num变成一个set
        # 这样每一次check current_num+1 在不在num_set里只take O(1)时间了
        # 因此这个方法时间是O(n^2) 空间是O(n)
        num_set=set(nums)
        for num in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

#再进行第二步优化以后的最优解
#思考后我们可以发现，其实我们不需要让每个num_set里的element都做一次起点
#我们只需要让num-1不在num_set里的num做起点就够了
#假设num set里有3 4 5 6 7 我们如果用蛮力方法的话，4 5 6 7都要分别做一次起点，4做起点就要check 5 6 7
#5 6做起点也要相应check后面的，重复access同一个element很多次

#但是对于num-1不在num set里的num，我们可以保证num一定是一个consecutive sequence的起点
#（真正的起点，因为num-1都不在numset里了）
#（当然也可能连num+1都不在numset里，那这样的话num就只是一个长度为1的sequence）
#而对于4 5 6 7它们对应的num-1都是在numset里的所以我们不用它们作为起点

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            # takes O(n) time
            num_set = set(nums)
            res = 1
            # for loop take O(n) time
            for num in num_set:
                if num - 1 not in num_set:
                    current_num = num
                    current_streak = 1
                    #这里看似while loop套在for loop里是一个N^2的时间
                    #但是其实因为我们只从num-1不在numset里的num作为起点
                    #所以一个numset里的num最多被while loop access 1次
                    #因此这个while loop在整个过程中也只有最多n个iteration
                    while current_num + 1 in num_set:
                        current_streak += 1
                        current_num = current_num + 1

                    res = max(res, current_streak)
            return res

#所以在这个方法里 list转换成set是O(n) time， for loop是O(n) time, while loop一个最多有n个iteration
#所以也是最多O(n) time
#因此总共time就是O(3n) 也就是O(n),space也是O(n)


#这是自己最开始写了一半没写出来，参考花花酱的相似思路后写出来的
#上面那种方法还是用hashset，set，这种方法用dict，hashtable
# 花花酱视频链接
# https://www.youtube.com/watch?v=rc2QdQ7U78I
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            #这个dict的key是nums里element的值，value是以key这个值为boundary的consecutive sequence
            #的长度，我们理论上只需要在key是一个boundary的时候，才记录以这个key为boundary的的consecutive
            #sequence的长度
            #例如，对于已经发现4 5 6 这个consecutive sequence以后，我们以后只需要update 4和6作为
            #key对应的dict里的value，也就是4或者6作为boundary的consecutive sequence的长度就可以了
            # dict里key是5对应的value以后都不用管了，因为以后不会再碰到和5相邻的数了

            #注意：这里的长度都是算自己在内的
            record={nums[0]:1}
            for num in nums[1:]:
                l=r=0
                #因为nums里可能有重复的，碰到一个之间碰到过的value 不管他直接continue
                if num in record:
                    continue
                #如果num+1或者num-1 也在record这个dict里的话把它们的value记录下来
                if num+1 in record:
                    r=record[num+1]
                if num-1 in record:
                    l=record[num-1]
                #如果num-1在record里，那么以num为边界的consecutive的sequence的长度就是l+1
                #如果num+1在record里，那么以num为边界的consecutive的sequence的长度就是r+1
                #如果num+1和num-1都在record里，那包含num的consecutive sequence的长度就是l+r+1
                #但是这种情况下因为num也不是boundary了所以也无所谓要不要记录上了
                record[num]=l+r+1
                #在update里以新碰到的num为boundary的consecutive sequence的长度以后
                #假设有num+1，那么num就是在这个sequence的左端点，更重要的是，我们还要update
                #这个sequence的右端点的value，因为现在加上了num，那么以右端点为boundary的sequence
                #的长度也应该+1了
                if num+1 in record:
                    record[num+record[num+1]]+=l+1
                #有num-1，num自己是右端点的情况同理
                if num-1 in record:
                    record[num-record[num-1]]+=r+1
            #最后整个dict的value过一遍，找到max之后return
            res=1
            for k,v in record.items():
                res=max(res,v)
            return res