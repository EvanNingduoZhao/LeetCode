def laberymith(n,m,obstacles,teleports):
    obstaclesSet=set()
    for o in obstacles:
        obstaclesSet.add((o[0],o[1]))
    teleDict={}
    # 为了防止出现传送会已经走过的地方的无尽循环情况，我们记录一下都到过哪里
    # 每次传送之前都check一下目的地是不是我们已经去过的地方，如果是就return False
    seen=set()
    for pair in teleports:
        teleDict[(pair[0],pair[1])]=(pair[2],pair[3])
    currPos=(0,0)
    seen.add(currPos)
    print('currPos', currPos)
    while True:
        # 如果到终点的就return True
        if currPos ==(n-1,m-1):
            return True
        # 看一下下一步要走到哪里
        nextPos=(currPos[0],currPos[1]+1)
        # check下一步是不是障碍或者出界了
        if nextPos in obstaclesSet or nextPos[1]==m:
            return False
        # 如果下一步要走到传送门了
        if nextPos in teleDict:
            # 且传送目的地还是走过的地方，那就return false
            if teleDict[nextPos] in seen:
                return False
            # 否则就传送过去
            else:
                currPos=teleDict[nextPos]
                seen.add(currPos)
            print('currPos',currPos)
            # 注意这里又个continue
            continue
        currPos=nextPos
        seen.add(currPos)
        print('currPos', currPos)

print(laberymith(3,4,[[1,1]],[[0,2,0,1],[0,3,2,0]]))