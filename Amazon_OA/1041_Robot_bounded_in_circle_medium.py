# 做这道题我们要先想清楚什么情况下机器人才是被bounded在一个circle里了
# 实际上两种情况会导致bounded in circle，第一种是走完一套instructions正好停在出发点
# 第二种是走完一套instructions以后没有停在出发点，但是面朝的方向不是开始时的北方了
# 第一种为什么会bounded in circle显而易见，主要说第二种的原因
# 假如说一套instructions走完以后相当于机器人向西走了一步且结束时还是面向西
# 那么只要走四套instructions就会让机器人回到原点，事实上只要是bounded in circle的，要不然是四套instructions之后回原点
# 要不然就是两套以后回。
# 所以我们需要做的就是完整地走一套instruction，看结束时机器人的位置和朝向是不是满足bounded in circle的条件
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 用一个list分别代表北东南西，注意这是有顺序的，即从北开始的顺时针顺序
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        # x和y代表横向纵向位置
        x=0
        y=0
        # d的值指的是directions里的index，即0代表北，1代表东
        d=0
        # 过一遍所有instruction
        for i in instructions:
            # 如果指令是向右转，那么d=(d+1)%4，注意%4可以保证原来朝向3即西时，向右转之后可以朝0即北
            if i=='R':
                d=(d+1)%4
            #  如果指令是向左转，那么为了避免deal with 负数，我们用+3而不是-1
            elif i=='L':
                d=(d+3)%4
            #   如果指令是往前走一步，那就按照现在面朝的方向update x和y
            else:
                x+=directions[d][0]
                y+=directions[d][1]
        # 如果走完一套instructions以后没有停在出发点，但是面朝的方向不是开始时的北方了，判定是bounded in circle
        if d!=0 and (x!=0 or y!=0):
            return True
        # 如果走完一套instructions正好停在出发点，判定是bounded in circle
        elif x==0 and y==0:
            return True
        # 否则不是bounded in circle
        else:
            return False