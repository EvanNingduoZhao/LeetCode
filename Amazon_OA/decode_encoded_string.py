# Question:
# Input is an encoded string and a rowNumber, and your purpose is designing a method to decode it
# How does the encoding work? For example, if string "my name is" will be encoded with rowNumber = 3,
# it will use a metrix to represent the original string first
# i.e.
#  m n e s _
#  _ y a _ _
#  _ _ _ m i
# You need read it from upper left to lower right, first char is in metrix[0][0] and
# second char should be in metrix[1][1] etc.
# and the input is constructed by this metrix line by line, means it will look like :
# "mnes__ya_____mi"
# If string "my name is" encoded with rowNumber = 4, it will look like:
#  m a i _ _
#  _ y m s _
#  _ _ _ e _
#  _ _ _ n _
# and the input will become "mai___yms____e____n_"
# You need decode the input string with rowNumber it provide and return the original string,
# remember to replace all '_' with space.
# 题目真实截图可以在桌面的 Amazon OA2 题库中找到

def decodestring(inp, n):
    matrix = []
    # 先算出来一个row有几个col，那么row和col的数量就都知道了，复原出来2D array
    # 之后按顺序读出来就好了
    numOfCol = int(len(inp)/n)
    for i in range(n):
        matrix.append(inp[i*numOfCol:i*numOfCol+numOfCol])
    for row in matrix:
        print(row)
    res = []
    row = 0
    col = 0
    firstRowPos = 0
    while True:
        res.append(matrix[row][col])
        if row==0 and col==numOfCol-1:
            break
        row+=1
        col+=1
        if row>=n or col>=numOfCol:
            row = 0
            firstRowPos+=1
            col = firstRowPos
    return "".join(res).replace("_"," ").strip()
print(decodestring("mai___yms____e____n_", 4))
print(decodestring("hlowrd_el_ol", 2))