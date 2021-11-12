def concatenateSUm(s,k):
    initialSum = ""
    counter = 0
    sum = 0
    for i in range(len(s)):
        sum+=int(s[i])
        print("sum is:",sum)
        counter+=1
        if counter==k:
            initialSum+=str(sum)
            print("str(sum) is:", str(sum))
            sum = 0
            counter = 0
    print("initial Sum is:",initialSum)
    while len(initialSum)>=k:
        print("in while loop")
        sum2 = 0
        counter2 = 0
        res = ""
        for i in range(len(initialSum)):
            sum2+=int(initialSum[i])
            print("sum2 is:", sum2)
            counter2+=1
            if counter2 == k:
                res+=str(sum2)
                sum2 = 0
                counter2 = 0
        initialSum = res
        print(initialSum)
    return initialSum

print(concatenateSUm("8979898799988789",3))