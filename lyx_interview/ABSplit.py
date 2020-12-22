def ABSplit(S):
    if S==None or len(S)<=3:
        return 0
    aCount=0
    for char in S:
        if char=='a':
            aCount+=1
    if aCount==0:
        n=len(S)
        return int((n-1)*(n-2)/2)
    else:
        if aCount%3!=0:
            return 0
        else:
            needNum=aCount/3
            aMet=0
            index=0
            while aMet<needNum:
                if S[index]=='a':
                    aMet+=1
                index+=1
            itemInBetween1=0
            while S[index]!='a':
                index+=1
                itemInBetween1+=1
            aMet = 0
            while aMet<needNum:
                if S[index]=='a':
                    aMet+=1
                index+=1
            itemInBetween2=0
            while S[index]!='a':
                index+=1
                itemInBetween2+=1
            return (itemInBetween1+1)*(itemInBetween2+1)

print(ABSplit('ababa'))