#这样的题目还是看到就应该想到快慢指针，慢指针记录seats中被左右两个有人的座位隔开的一段椅子中左边
#椅子的位置，快指针不断往前走去找右边椅子的位置，找到后用（j-i）/2的方法算出来如果坐在这段椅子中间
#最大的和别人的距离是多少，keep updating max for every new group we have seen.
#这个方法要注意两点，第一seats的开头和结尾也可以左右一个group的起始点，如果是这种group的话，group
#内最大距离为j-i（此时i为0）or j-i（此时j为len（seats）-1）
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dis=1
        max=1
        i=0
        for j in range(0,len(seats)):
            if seats[j]==1:
                if seats[i]==0:
                    dis=j-i
                else:
                    dis=(j-i)/2
                if dis>max:
                    max=dis
                i=j
                continue
            if j==len(seats)-1:
                dis=j-i
                if dis>max:
                    max=dis
        return int(max)