#以下代码是按照 这个视频里的思路来写的 https://www.youtube.com/watch?v=ZEgoEf8HGKI
# 首先一个unit能不能存水，取决于它上下左右的四个unit是不是都比它高，具体能存多少水则取决与它周围的四个unit里最矮的那个
# 那么我们首先就可以知道在四边edge上的unit都是不可能存水的
# 我们先把所有edge上的unit的height和它们的行列坐标都push到一个minHeap里
# 之后我们开始从最小的height的unit开始向外pop，每pop出来一个unit以后，我们就check它上下左右四个邻居，（通过维持visited
# 来保证每个unit都只被遍历一次）如果刚被pop出来的unit A的某一个邻居 B的height是要小于它的话，那么这个邻居就是可以存水的，且能
# 存的水的量是A的height-B的height。
# 为什么这个结论是成立的呢？因为A是从minHeap里pop出来的，它是目前我们见到且还没处理过的unit里最小的一个，根据这个性质我们可以
# 推导出两个结论：
# 1.同样也在edge上，但是比A小的C，也就是在A之前被pop出来的，被这种edge unit作为wall的pool P里的element就算是也以A作wall，
# 我们照样不会算错那个P里临着A的unit的储水量，因为这个unit的储水量在pop C出来以后一连串的处理的时候就已经被visit了

# 2.以A做wall的还没有被visited的pool的element，它的height只要比A小，它就一定能装水，因为漏水最终一定是从edge的某一个unit
# 漏出去的，但是以比A小的edge element为wall的pool里的unit我们都处理过了，剩下的edge element都比A大，所以只要比A height小的
# unit装的水是一定不会漏出去的，而且装水量是取决与A的height的

#假设A的height是5 A的邻居不是edge unit的B的height是3， B的邻居C （C不和A直接相邻）能装多少水其实还是取决A的高度
#因为假设C比5大或等于5，那B能装多少水肯定是取决与它更矮的那个wall也就是A的。假设C小于5，say 2，那它能装的水也是取决于A的
#height 5的而不是B的height 3。因此如果B小于A，在算出了B里能装多少水以后要把B的height update成A的height，跟B的坐标一起
#push到heap里，用A的height来算B自己的neighbor能装多少水
# 实际上一个位置A上方能装的水等于它上下左右四个方向上分别的那四个最高点里最矮的那个的高度-A位置自己的高度
# 想明白这件事不是很容易，可以先从一个2D的这个问题开始思考，之后结论是可以tranlate到3D的

# 那么我们最好的方式就是从grid的四个边入手，不断把边界像grid内部推进，用一个minHeap来存目前边界上的所有位置的高度即其坐标
# （注意这里我们所说的边界是动态的，是不断向grid内部推进的）那么我们每次从heap里pop出来的就是目前整个边界上最矮的那个位置
# 而因为边界内部所有的位置上方能储水的高度都是由它的上下左右四个方向上的分别四个最高点中的最矮的那个决定的，
# 那么对于紧邻着刚从heap中pop出来的这个目前最矮的边界位置A，和它直接相邻的边界内部的位置B上方的储水高度一定是由它决定的
# 因为A一定是B上下左右四个方向上的分别四个最高点中的最矮的那个，假设ABC三个位置是从下到上摞着排列的，A在最下面
# 那么如果按照上面的例子B的高度低于A，那么B一定不是C下方的最高点，A才是，而C在除了下方的A以外的其他三个方向上
# 都有比A高的位置，因为其他三个方向上还有边界位置，而A是最矮的边界位置，所以其他三个方向上的边界位置一定高于A
# （注意C的上方能够储水的高度的是由它的上下左右四个方向上的分别四个最高点中的最矮的那个，C下方的最高点一定是A了
# 但是它其他三个方向的最高点不一定是其他三个方向上的边界，可能是边界内部我们至今还没有遇到过的位置，但是如果真的又这样的位置
# 也没关系，因为它们都比这其他三个方向的边界高，那就一定比A高，所以决定C上方存水高度的还是A）
# 但是如果反之B比A高，那么首先B不能存水了，且在这个方向上的动态边界的高度要变成B的高度了，因为此时决定C上方存水高度的是B了
import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        else:
            res = 0
            minHeap = []
            numOfRows = len(heightMap)
            numOfCols = len(heightMap[0])
            # push all edge elements into the heap
            for i in range(0, numOfCols):
                heapq.heappush(minHeap, (heightMap[0][i], (0, i)))
                heapq.heappush(minHeap, (heightMap[numOfRows - 1][i], (numOfRows - 1, i)))
            for i in range(1, numOfRows - 1):
                heapq.heappush(minHeap, (heightMap[i][0], (i, 0)))
                heapq.heappush(minHeap, (heightMap[i][numOfCols - 1], (i, numOfCols - 1)))

            # right,down,left,up
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            visited = set()
            while minHeap:
                height, (row, col) = heapq.heappop(minHeap)
                #用一个for loop直接解决四个方向，这样写代码很简洁
                for d in directions:
                    r = row + d[0]
                    c = col + d[1]
                    # 如果(r,c)不是edge上的bar且没有被visited过
                    if r > 0 and r < numOfRows - 1 and c > 0 and c < numOfCols - 1 and (r, c) not in visited:
                        if heightMap[r][c] <= height:
                            # 如果刚pop出来的bar的邻居能装住水，把装水量加到res上
                            res += height - heightMap[r][c]
                            # 把刚pop出来的bar的高度和这个能装水的邻居的坐标push到minHeap里
                            # 这就是A比B高的情况，边界的位置更新成B的位置，但是高度还得是A的高度
                            heapq.heappush(minHeap, (height, (r, c)))
                        else:
                            # 这就是B比A高的情况，边界的位置更新成B的位置，但是高度也是B的高度
                            heapq.heappush(minHeap, (heightMap[r][c], (r, c)))
                        # 把新push到heap里的bar label成visited
                        visited.add((r, c))
            return res

