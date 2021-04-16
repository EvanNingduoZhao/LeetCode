# 这道题首先要想明白一个道理，我们hire一组人，为了让每个人得到的wage和它们的quality是成正比的
# 对于每个人而言，得到的wage per unit of quality都是相等的，那么这一组人的得到的wage per unit of quality
# 是根据谁的expected min wage per quality得到的呢，答案是这一组里expected min wage per quality最高的那个人
# 举个例子假设一组里有两个人，一个人的q是10，期望工资是5。另一个人的q是5但是期望工资是10，
# 那么第一个人的w/q ratio是0.5,第二个人的ratio是2
# 我想要hire它俩，只能给第一个人20，第二个人10。可以看出每个unit of q值多少钱是由这一组里那个w/q ratio最高的人
# 的w/q ratio决定的

# 在一组人里，一定又至少一个人得到的是他的expected min wage，这是一定的，我们不能漫天给高价
# 那么我们如果hire一个人 A，并且给这个人它想要的expected min wage的话，那么我们就只能hire w/q ratio比他底的人了

#因此我们解这道题的思路就是，让每一个人都当一次A，如果这个人当A的情况下有k-1个人的w/q ratio比他的底
# 那么我们就hire这k-1个人加上这个A，给每个unit of q发A的w/q ratio那么多钱

# 如果这个人当A的情况下只有少于k-1个人的w/q ratio比他的低，那这样就凑不齐k个人了，说明这个人不能当A

#如果这个人当A的情况下，有多于k-1个人的w/q ratio比他的低，那么我们取这些人里q最低的k-1个
# hire A和这k-1个人，因为A决定了给每个unit of q我们发多少钱，那么我们除了A以外想要的一定是q的总和最低的k-1个人

#实际上我们一只用一个maxHeap来存目前w/q ratio比A的低的里q最小的k-1个，具体看下面comment
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        # 我们先用一个list of tuples存每个worker的ratio，expected min wage和q
        #并将这个list按照每个worker的ratio增序排列
        workers=[]
        for i in range(0,len(quality)):
            ratio=wage[i]/quality[i]
            workers.append((ratio,wage[i],quality[i]))
        workers.sort()
        heap=[]
        # qualitySum是用来存目前heap里的k个人（包括A和k-1个q最小的）的q的sum
        qualitySum=0
        res=float('inf')

        for ratio, w, q in workers:
            # 我们想用的是maxHeap，但是heapq默认是minHeap，所以我们把q的负值push进去
            heapq.heappush(heap,-q)
            qualitySum+=q
            if len(heap) > K:
                qualitySum-=heapq.heappop(heap)*(-1)
            if len(heap)==K:
                # 计算总工资的时候我们永远是按照刚push进来的那个人的ratio乘以总quaility sum来计算的
                # 因为我们把workers按ratio增序排列了，所以刚push进来的那个人ratio一定是已经进来的人里
                # ratio最大的，而一组人里每个unit of quality值的工钱就是由ratio最大的那个人的ratio决定的
                # 这里还有一个小问题，就是如果刚进来的那个worker是quality最大的，在41行被pop出去了怎么办？
                # 这样的话heap里剩下的k个worker里实际上是没有他的，但是我们还在按照他的ratio来算总工钱
                # 但是这样其实是没事的，因为目前这个k个worker实际上在上一个worker被push进来时就出现过一次了
                #  且那时我们是按照上一个worker的ratio来算的总工钱，这次我们用刚进来的那个worker的ratio
                # 给同样一帮人算总工钱，但是因为刚进来的那个人的ratio一定是大于等于上一个人的，所以算出来
                # 的总工钱只会多不会少，因此不会导致res update 所以没关系
                res=min(res,ratio*qualitySum)
        return res