def sumOfReversed(arr):
    res=0
    for num in arr:
        queue=[]
        numString=str(num)
        zeroCount=0
        for i in numString:
            if i=='0':
                zeroCount+=1
            else:
                queue.insert(0,int(i))
        base=1
        count=0
        while count<zeroCount:
            base*=10
            count+=1
        reversedNum=0
        while queue:
            reversedNum+=queue.pop()*base
            base*=10
        print(reversedNum)
        res+=reversedNum
    return res

arr=[7,234,58100]
print(sumOfReversed(arr))
