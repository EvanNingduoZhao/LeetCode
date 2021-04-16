def minRound(N,k):
    if N==0:
        return -1
    oneChip=0
    allIn=0
    while N!=1 and k>0:
        if N%2==1 or N==2:
            N-=1
            oneChip+=1
        else:
            N/=2
            allIn+=1
            k-=1
    oneChip+=N-1
    return oneChip+allIn

print(minRound(8,0))