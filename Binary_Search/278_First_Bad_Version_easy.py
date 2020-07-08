#上面这个是自己写的土办法，下面的是模版的标准写法，看一下自己的土办法有利于理解标准的模版方法
# 这道题是一个典型的，光靠看mid自己是看不出来mid自己是不是target的问题，必须还要看左边的邻居
# 才能确定mid是不是target的题（因为作为第一个bad version不但需要自己是bad，还需要自己左边的
# 邻居是good）
# 如果把这道题改成找到最后一个good version，那么这就是于是必须要看右边邻居的题了

# 对于这种题，我们要用这个note里的模版二（这个模版里说的我这道题用的code是看右边邻居的版本的code
# 我认为是这个网页里写错了，这个应该是看左边邻居的code）
# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/937/

#以下是自己写的土办法
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #首先end为什么是n：因为这道题的input不是一个list，就是一个int n告诉你现在一共有几个version
        #所以最后一个version就是n
        start=1
        end=n
        #对于binary search而言，whileloop是小于还是小于等于是很关键的一件事：
        #在whileloop里面这样写的前提下，这里必须要用小于等于，原因如下：（先看loop里面内容的comment）
        #binary search的问题一般要考虑两种ending senario：
        # 第一种：最后剩三个element，end-start=2
        # 这种情况下，mid=start+1，mid是夹在start和end的中间的，那么如果这时mid是bad的，且start是
        # good的，那么直接return mid，如果不符合这种情况的话，那可能是以下两种sub情况之一，
        # （1）mid自己是bad的，start是第一个bad，end是good：
        #  这种情况下，属于下面的else里的else，即end=mid-1=start，那么这时start和end重合，
        #  while loop，那么再进行一次时，mid=start=end，mid是bad的，且它前一个是good的，return mid
        #  这种情况就必须要求我们while loop是小于等于，只有这样，在start=end的时候才会再执行一次
        #   并且在这一次执行中找出target
        # （2）mid自己是good的，start也是good，end是第一个bad version：
        # 那么start=mid+1=end了，这时start=end，while loop还得进行一次，
        # 那么再进行一次时，mid=start=end，mid是bad的，且它前一个是good的，return mid，
        # 这里依旧需要我们的while loop是小于等于，让start和end重合是能再执行一次。
        # 第二种：最后剩下两个element，end-start=1
        # 这种情况下依然有两种sub 情况：
        # （1）start是target：
        # 这时，mid=start，且mid前面一个是good，直接return mid
        # （2）end是target：
        # 开始mid=start，发现mid是个good，那么start=mid+1=end，start和end重合了，跟第一种情况的
        # 两种sub情况一样，需要whileloop是小于等于，让whileloop再执行一次才能找到target是end

        # 综上，whileloop必须得是小于等于
       while start<=end:
            mid=(start+end)//2
            #如果mid自己不是Bad的，那么要找的第一个bad的一定是在mid右边
            #mid自己已经排除嫌疑了，所以把start调成mid+1。
            if isBadVersion(mid) == False:
                start=mid+1
            #如果mid自己是bad的，那么它可能是第一个bad的version，也可能第一个bad的version
            #在它前面就已经出现过了
            else:
                #因此我们首先check mid紧邻着的左边的item是不是good的，如果是的话，那说明
                #mid是第一个bad，那么mid就是我们要找的target
                if isBadVersion(mid-1)==False:
                    return mid
                #如果它紧邻着的左边的item不是good的话，那说明mid自己肯定不是第一个bad
                #因此mid自己排除的嫌疑，end=mid-1
                else:
                    end=mid-1

# 以下是针对这种题的标准模版解法，这种还是比我的土办法好的，
# 首先它好想，不用针对每一道题都想一个特殊的判定，只要判定了题目的类型
# 直接套用对应的模版就好了。其次，土办法每次见到了是bad的mid还要再check以下
# mid前面那个是不是good，这种标准方法就不用，节省时间。

# 这种标准方法的核心思想是这样的：
# 我每次根据mid的值，改我的start和end的时候，我都把它们改成包含所有有嫌疑的items的inclusive的边界
# 而且因为它们俩最终一定会重合，即terminate的时候一定是start=end的不会出现错开的情况（这个一定会
# 以重合结束，不可能以错开结束是这个方法最重要的性质，而且必须是while是小于，start=mid+1，end=mid
# 才能实现这个性质，必须这么写什么都不能改，当然如果题目改成找到最后一个good的version，那么得改成，当mid是bad
# 时，end=mid-1，因为mid是bad了它自己的嫌疑排除了，当mid是good时，start=mid，因为我们不知道
# mid是不是之后一个good，所以mid还是有嫌疑，因此start=mid，这样还是可以保证最后两者以重合结束
# ，因为这样改实际上属于是对称地改，是不会影响以重合为结尾的这个性质的）

# 因此，那么因为start和end是inclusive的boundary of所有有嫌疑的items，每次换start或者end的时候
# 都只排除完全没有嫌疑的，那么如果input里是保证有target的话，那么当start和end最后重合，两者指向
# 一个element时，那只剩下它有嫌疑，那一定target就是他了。这个道理就相等于，我知道一定有一个罪犯，
# 但有嫌疑的人只有一个，那么这个人一定就是罪犯。当然如果不能保证input里一定有target，那么最后还需要
# 进行一步post processing，具体如果poset processing见下面网页里的模版2的最后
# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/937/
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1
        end=n
        # 这里之所以用小于是因为可以保证terminate的时候是start和end重合的时候，
        # 可以保证只要start和end重合，start和end指向的那个item就一定是target
        # 当然前提是，input里是保证有target的
        while start<end:
            mid=start+(end-start)//2
            #如果mid自己不是Bad的，那么要找的第一个bad的一定是在mid右边
            #所以把start调成mid+1，mid自己已经排除嫌疑了
            if isBadVersion(mid) == False:
                start=mid+1
            #但是如果mid自己是bad，那么它自己也有可能是第一个bad的version
            #他自己还是有嫌疑，不能排除在外，因此end=mid
            else:
                end=mid
        #为什么能保证在start和end重合是他俩指的那一个item就是target。因为在以下所有情况中都可以保证
        # 第一种：最后剩三个element，end-start=2
        # 这种情况下，mid=start+1，mid是夹在start和end的中间的，第一种情况有两种sub情况
        # （1）如果这时mid是bad的，（mid有可能是第一个bad，也有可能是start是第一个bad）：
        # 那么就end=mid了，变成了一个end-start=1的情况，这种情况我们在下面讨论。
        # （2）如果这时mid是good的，那么肯定end是第一个bad version：
        # 那么start=mid+1=end，直接return start

        # 第二种：最后剩下两个element，end-start=1
        # 这种情况下依然有两种sub 情况：
        # （1）start是target：
        # 这时，mid是start，mid就是bad，那么end=mid=start，直接return start
        # （2）end是target：
        # 开始mid还是start，发现mid是个good，那么start=mid+1=end，start和end重合了，return start

        # 综上，在所有情况中，只要start和end一重合，他俩指向的就一定是正确结果

        return start