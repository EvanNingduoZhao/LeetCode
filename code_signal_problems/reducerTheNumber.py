def reduceTheNumber(number,k):
    # print(number)
    if len(number)<=k:
        return number
    i=k
    newNum=''
    while i<len(number):
        sum=0
        j=i-k
        while j<i:
            sum+=int(number[j])
            j+=1
        newNum+=str(sum)
        i+=k
    if i-k<len(number):
        sum=0
        i=i-k
        while i <len(number):
            sum+=int(number[i])
            i+=1
        newNum+=str(sum)
    return reduceTheNumber(newNum,k)

print(reduceTheNumber('1111122222',3))
