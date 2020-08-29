#这道题要用一个两头指针方法来做
#首先我们要知道两个wall组成的container能装的水的量是由更矮的那个wall决定的
#因此container的height就是shorter wall的height，container的width就是两个
#wall之间的距离
#其次我们要确定的是，我们必须把整个list都遍历完才能保证我们得到正确答案，因为
#有可能在list的正中间的两个wall就是10000和10000的高度
#那么现在的问题就是我们该怎么移动左右两个指针呢，答案是我们每次都只把指向shorter wall
#的那个指针往内侧移动。因为我们如果动的是指向更高的那个wall的指针的话，就算动了之后
#指针指向的那堵墙比原来的higher wall还高，但是由于container的height是由
#shorter wall 决定的，新的higher wall多高也没用，而且把指向higher wall的指针
#向内移动还白白牺牲了container的width。
#还有一个重要的问题即，当目前container的两堵墙高度一样时该怎么办？
#假设两堵高度一样的墙是A和B，那么只有在A和B之间有C和D两堵墙且C和D的高度都大于A和B
#C和D才有可能组成一个容积大于AB组成的container的容积的容器。根据我们算法，在指针
#指向A和B时不管我们先移动哪个指针，最后两个指针都会在某一刻指向C和D，因此在指针
#指向A和B时，先动哪个无所谓
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right=len(height)-1
        left=0
        res=0
        while left<right:
            shorterWall=min(height[left],height[right])
            res=max(res,shorterWall*(right-left))
            if height[left]<height[right]:
                left+=1
            #这里的else里包含了A和B两堵墙一样高的情况
            else:
                right-=1
        return res