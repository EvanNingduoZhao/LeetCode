#这种问题要用快慢指针来做，即慢指针存着目前这个group的开头是什么，快指针一直往前走，直到快指针
#对应的和快指针的下一个对应的不相等或快指针到尾巴了，那么说明一个group结束了，这时用i-j+1算
#以下这个group的长度，如果大于等于3就可以append到ans里
#这种方法的好处是不用时刻更新count，只要等一个group结束了算一下count就行
class Solution:
    def largeGroupPositions(S):
        if len(S)<=2:
            return []
        else:
            ans=[]
            i=0
            for j in range(0,len(S)):
                if j==len(S)-1 or S[j]!=S[j+1]:
                    if j-i+1>=3:
                        ans.append([i,j])
                    i=j+1
            return ans

    def mylargeGroupPositions(S):
        if len(S)<=2:
            return []
        else:
            start=0
            end=0
            ans=[]
            count=1
            interest=S[0]
            have=False
            for i in range(1,len(S)-1):
                if S[i]==interest:
                    count+=1
                    print("count is: "+str(count))
                    if count>=3:
                        have=True
                        end=i
                else:
                    if have==True:
                        ans.append([start,end])
                        print("ans is: "+str(ans))
                    have=False
                    interest=S[i]
                    count=1
                    start=i
            print("after the for loop, ans is: " +str(ans))
            if S[len(S)-1]==interest:
                count+=1
                print("after adding the last one count is: "+str(count))
                if count>=3:
                    end=len(S)-1
                    ans.append([start,end])
            else:
                if have==True:
                    ans.append([start,end])
            return ans

    s="bababbaaab"
    print(largeGroupPositions(s))