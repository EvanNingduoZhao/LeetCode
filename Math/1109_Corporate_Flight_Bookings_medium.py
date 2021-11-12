# 这道题涉及到了prefix sum的另一种使用方法
# 即如果你用下面的错误方法来写的话，假设bookings的长度是m，那么时间复杂度可以说是O(m*n)因为一个booking可以覆盖的区间的最大长度是n
# 相比之下下面的这个使用prefix sum的方法就很好了
# 什么叫prefix fix sum，实际上就是给你一个list比如[10，20，30，40]，那么他的prefix sum list就是[10,30,60,100],即prefixSum[i]=sum(list[:i+1])
# 那么也就是说，如果我给list[i]加上10，那么在prefixSum里prefixSum[i:]里的所有item都会+10，进一步来说如果我在给list[j]减10
# 那么在prefixSum里的效果就是只有prefixSum[i:j]这些element加10了
# 因此我们就利用这个手段，对于每一个booking，我们给flights[b[0]-1]加上b[2],给flight[b[1]]减去b[2],
# 注意上一行的说明是考虑进去了bookings里的index都是1 based的，所以要用flights[b[0]-1]
# 对于每个booking都这样做一遍之后，在算一下处理过后的flights的prefix sum就可以得到刚才的错误方法得到的一样的结果了
# 但是这次我们的时间复杂度只是O(n+m)
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0]*n
        for b in bookings:
            flights[b[0]-1]+=b[2]
            if b[1]<len(flights):
                flights[b[1]]-=b[2]
        for i in range(1,len(flights)):
            flights[i]+=flights[i-1]
        return flights

# 错误方法
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0]*n
        for b in bookings:
            for i in range(b[0]-1,b[1]):
                flights[i]+=b[2]
        return flights