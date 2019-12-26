#这不是一个DP问题
#蛮力方法一定是O（n squared）的时间复杂度
#为了得到一个O(n)的算法，我们在每看到一个新的array element的时候就要以O（1）的时间复杂度
#来把他和之前所有看到过的elements的组合能达到的profit都考虑一遍
#（只需要看当前的和之前看到的组合就够了，不用考虑当前的和还没看到的，因为只能先buy再sell）
#实际上，看当前的和之前看过的所有的element的组合，也不用看所有之前看过的elements，只用看
#当前的和之前看过的里面的最小的组合能产生多少profit就够了，因此要keep一个min variable
#在新看到和一个element后算出来如果以它为sell price，那么buy price必须小于多少才能超过目前的
#max profit，这个要找的临界值我们叫它target。只要把目前的min和target比较即可，如果min小于target
#则max profit更新为当前的element-min
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        else:
            mp=0
            min=prices[0]
            for price in prices:
                target=price-mp
                if min<target:
                    mp=price-min
                if price<min:
                    min=price
        return mp