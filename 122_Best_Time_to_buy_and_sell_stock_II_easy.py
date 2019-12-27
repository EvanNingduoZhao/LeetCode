#只有后一天的价格比前一天的高 就把后一天和前一天的差值加到总profit里
#为什么这样做是work的：
#在价格连续涨的情况下，这样相当于把连涨的每一段分开加在一起
#在[1，5，3，6]这种情况下，注意5-1=4，6-3=3 3+4=7 这样7是大于6-1=5的所以在波动上涨时
#要把每一次涨的利润都拿到而不是只算最高和最低的差
#很明显我的方法是可以做到拿到每一次涨的利润的

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0 or len (prices)==1:
            return 0
        else:
            profit=0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    profit+=prices[i]-prices[i-1]
            return profit