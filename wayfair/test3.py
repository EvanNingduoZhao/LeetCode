neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
currPos = [3,5]
for neighbor in neighbors:
    position = zip(currPos,neighbor)
    for p in position:
        print(p)
    pos=[sum(x)for x in zip(currPos,neighbor)]
    # print(pos)

# pos = zip(currPos,directions)
# for i in pos:
#     print(i)
# print(zip(currPos,directions))
# print([sum(x) for x in zip(currPos,directions)])