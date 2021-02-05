def digitAnagrams(a):
    res={}
    for num in a:
        count=[0]*10
        for d in str(num):
            count[int(d)]+=1
        count=tuple(count)
        if count in res:
            res[count]+=1
        else:
            res[count]=1
    sum=0
    for c in res.values():
       if c>=2:
           # 假设互为anagrams的一组数有4个
           # 那么第一个可以分别和2 3 4组成一对
           # 第二个可以和3 4组成一对
           # 第三个只能和4组成一对
           # 所以对于一组有四个的anagrams而言有3+2+1个pair，
           # （1+c-1）(c-1)/2
           sum+=c*(c-1)/2
    return sum

a=[25,35,872,228,53,278,872]
print(digitAnagrams(a))