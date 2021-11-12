import heapq
# 在新来的batch是buy时，我们要把新的buy batch的price和已经见过的sell order里price最小的比
# 因此sell heaq应该是个min heap。相反在新来的batch是sell时，我们要把新的sell batch的price和已经见过的
# buy order里price最小的比因此buy heaq应该是个max heap
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
#         maxHeap
        buyHeap = []
#     minHeap
        sellHeap = []
        for price,amount,orderType in orders:
#             新来的是a batch of sell
            if orderType == 1:
                # 只要新来的batch的amount还没有被全部满足就继续
                while amount>0:
                    # 如果buyheap不是空的，且buy里最高的price大于等于新来的sell batch的price
                    # 注意buyheap是maxheap，我们要给pop出来的element乘上-1
                    if buyHeap and (-1)*buyHeap[0][0]>=price:
                        # 这里有两种情况
                        # 第一种是buy batch里的那个price的order的数量就大于sell batch的数量
                        # 能够满足所有的sell order，且满足了以后这个buy batch的数量还不会被减到0
                        # 那么直接在buy batch的数量里减去sell bacth的数量之后break即可
                        if buyHeap[0][1]>amount:
                            buyHeap[0][1]-=amount
                            break
                        # 第二种是buy batch里的那个price的order数量小于等于sell batch的数量
                        # 不能满足所有的sell order，或者可以满足，但是满足了以后buy batch的数量
                        # 正好减到0了，需要被pop出heap了。那么就能满足多少满足多少，满足了多少就在
                        # amount里减去多少之后把这个buy batch从heap里pop掉。开启while loop的下一个
                        # iteration
                        else:
                            amount-=buyHeap[0][1]
                            heapq.heappop(buyHeap)
                    # 若果buyheap是空的，或者buy里最高的price也小于新来的sell batch的price
                    else:
                        # 那就只能把sell batch直接push到sell heap上了
                        sellTuple = [price,amount]
                        heapq.heappush(sellHeap,sellTuple)
                        break
#             a batch of buy
            else:
                while amount>0:
                    if sellHeap and sellHeap[0][0]<=price:
                        if sellHeap[0][1]>amount:
                            sellHeap[0][1]-=amount
                            break
                        else:
                            amount-=sellHeap[0][1]
                            heapq.heappop(sellHeap)
                    else:
                        # 注意buyheap是maxheap，我们要给push进去的element乘上-1
                        buyTuple = [(-1)*price, amount]
                        heapq.heappush(buyHeap,buyTuple)
                        break
        totalRemainingOrders = 0
        for batch in buyHeap+sellHeap:
            totalRemainingOrders+=batch[1]%(10**9+7)
        return totalRemainingOrders%(10**9+7)