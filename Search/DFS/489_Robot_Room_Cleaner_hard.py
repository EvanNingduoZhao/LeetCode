# 以下这些code是题目里给的robot这个api的code
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
#         up right down left
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        # 我们把visited的位置也视为是block的
        visited=set()

        # 这个goback function的作用就是让robot朝着它现在正在facing的方向的相反方向后退一格并保持
        # facing现在正在facing的方向
        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        # 这个backTrack function实际上是用来控制机器人移动的，但是在移动的过程中
        # 让机器人可以回到它之前所在的位置
        def backTrack(cell,currDir):
            # 我们每到一格新的位置就是clean那里，并且把这个新位置加到visited里
            robot.clean()
            visited.add(cell)
            # 之后robot要从自己目前正在facing的方向开始，依次尝试，如果某个方向上的下一个cell
            # 不是block也还没有被visited，那么它就要去那里，之后再继续向深探索
            # 说白了这就是个DFS，四个方向就相当于一个node有四个child，把一个child的整个subtree都走完了
            # 才会开始走第二个child的subtree
            for i in range(0,4):
                # 注意i是从0开始的，所以currDir+0在modulo 4的结果还是currDir，因此newDir是从
                # 机器人目前就在facing的方向开始尝试的
                newDir=(currDir+i)%4
                # 计算处目前newDir方向的下一个cell的坐标
                newCell=(cell[0]+directions[newDir][0],cell[1]+directions[newDir][1])
                # 如果这个newCell没有被visited过，且还不是一个block，那么这个newCell就是我们下一个要去的地方
                # 注意这里我们用move来检测newCell是不是一个block，如果不是的话，move就直接让robot往前走一格了
                if newCell not in visited and robot.move():
                    # 在newCell上call backTrack，注意param还有一个就是目前正在facing的direction
                    # 机器人正在facing的dir就是这样传递的
                    backTrack(newCell,newDir)
                    # 结束了探索一个child的subtree以后我们用goback，回到上一个位置处，准备继续探索
                    # 上一个node里还没有探索过的其他dirs。这里的goback其实类似stack pop的作用
                    goback()
                # 刚才说准备探索剩下还没探索过的其他dirs，这里就是负责转向的，转到facing下一个要探索的dir
                # 注意我们在direactions里写的方向的循序就是上右下左，这次转完了以后就进入64行for loop的下一个
                # iteration了，i increment了1，那么newDir也就指向directions里的下一个方向了。最重要的是
                # 因为我们一直从facing上开始，之后不断turnRight，是顺时针转，
                # directions的循序上右下左，是从上开始，也是顺时针，所以newDir永远都指向目前robot正在face的方向
                # 这个设计才是这个code的精妙之处
                robot.turnRight()
        # 让机器人从（0，0）位置facing上的状态开始
        backTrack((0,0),0)