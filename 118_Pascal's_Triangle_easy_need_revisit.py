
#下面的方法正确但是只超过6% 学了DP以后要revisit再做一次
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return None
        elif numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            ans=[[1],[1,1]]
            numr=2
            while(numr<numRows):
                newlist=[1]
                nume=1
                while(nume<numr):
                    newlist.append(ans[numr-1][nume-1]+ans[numr-1][nume])
                    nume+=1
                newlist.append(1)
                ans.append(newlist)
                numr+=1
            return ans