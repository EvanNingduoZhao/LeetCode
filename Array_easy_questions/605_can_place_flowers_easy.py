
#对于中间的spots 有3个连在一起的0，就可以多种一棵，有了三个以后再每多有两个0就又可以多种一棵。
#对于flowerbed开头的和结尾的spots只要有两个0就可以种一个（eg 00101 这种情况下就可以在第一个0
# 的地方种一个）所以我们让zerocount起始=1，这样只要再加两个0就可以达到3（可以让count+1的标准）
#for loop结束以后如果zerocount还==2的话就说明是这样的情况1010100（最后一位可以在种一个）
#因此count再加一
#注意本题要return的是boolean
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zerocount=1
        count=0
        for i in range(0,len(flowerbed)):
            if flowerbed[i]==0:
                zerocount+=1
                if zerocount==3:
                    count+=1
                    zerocount-=2
            else:
                zerocount=0
        if zerocount==2:
            count+=1
        if count>=n:
            return True
        else:
            return False