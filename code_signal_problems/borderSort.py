import heapq
import math
def borderSort(matrix):
    heap=[]
    n=len(matrix)
    currRow=0
    currCol=0
    # while loop的每一次iteration就是一层
    while currRow<math.ceil(n/2):
        # 先把一层的所有内容都push到heap里
        for c in range(currCol,n-currCol):
            # 放进去最上面的一行
            heapq.heappush(heap,matrix[currRow][c])
            # 放进去最下面的一行
            heapq.heappush(heap,matrix[n-currRow-1][c])
        for r in range(currRow+1,n-currRow-1):
            # 放进去最左面的一行
            heapq.heappush(heap,matrix[r][currCol])
            # 放进去最右面的一行
            heapq.heappush(heap,matrix[r][n-currCol-1])
        # 之后再按照顺时针的循序把pop出来的挨个放进对应的位置里
        for c in range(currCol,n-currCol):
            matrix[currRow][c]=heapq.heappop(heap)
        for r in range(currRow+1,n-currRow-1):
            matrix[r][n-currCol-1]=heapq.heappop(heap)
        for c in reversed(range(currCol,n-currCol)):
            matrix[n-currRow-1][c] = heapq.heappop(heap)
        for r in reversed(range(currRow+1,n-currRow-1)):
            matrix[r][currCol] = heapq.heappop(heap)
        # increment currCol和currRow为下一次iteration作准备
        currCol+=1
        currRow+=1
    return matrix


matrix=[[9,7,4,5],
        [1,6,2,-6],
        [12,20,2,0],
        [-5,-6,7,-2]]
for row in matrix:
    print(row)
print('+++++++++++++++++++')
res=borderSort(matrix)
for row in res:
    print(row)
