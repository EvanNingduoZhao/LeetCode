# Given a string made up to integers 0 to 9, count the number of ways to split the string into
# unique prime numbers in the range of 2 to 1000 inclusive, using up all the characters in the string.
# e.g "31" -> return 1
# e.g. "11373" -> return 6
# e.g. "1147" -> return 1 not 2, cause 1147 > 1000

# 用来check一个数字a是不是prime，从2到这个数的平方根一个一个过，看这个数字a能不能整除这个数，如果能
# 就不是prime
def isPrime(num):
    if num<2:
        return False
    sqrt = num**0.5
    # print("int(sqrt) is: ", int(sqrt))
    for i in range(2,int(sqrt)+1):
        # print("i is: ",i)
        if num%i == 0:
            return False
    return True

# 这道题我们用一个recursion，即top down的DP来解决
# subproblem是这样的：对于11373而言，它可以被分割成primes的方法的数量是这样算的
# 首先看11373以第一位数字1开头的substring，有几个是小于1000的prime，答案是11，和113
# 那么实际上11373可以被分成primes的方法的数量就等于373（开头的11确定了）和73（开头的113确定了）
# 各自对应的可以分成primes的方法的数量
# 373有四种分法[3,7,3] [3,73] [37,3] [373]， 73有两种分法[7,3] [73]
# 因此11373一共有6种分法[11，3,7,3] [11，3,73] [11，37,3] [11，373] [113，7,3] [113，73]
# 每一次invoke下面这个recursive function我们求的都是对于从startIndex开始的这个s的substring而言
# 有多少种分法，我们还加入了memoization，即对于每一个startIndex，我们把它对应的分法数量算出来一次后
# 就存到numOfWays里，下次如果还需要的话直接从numOfWays里找，numOfWays的初始值是每个element都是-1
# 它的element i是：startIndex是i的s的substring有多少种分法。如果numOfWays[i]!=-1,那么说明我们把
# startIndex是i的substring的分法已经算出来过一次并存到numOfWays里了，直接return numOfWays[i]就行
# 对于一个input string而言，可以分割成primes的方法的数量=
def countNumOfWays(s,startIndex,numOfWays):
    print("numOfWays is: ", numOfWays)
    print("startIndex is: ",startIndex)
    print("startDigit is: ",s[startIndex])
    if numOfWays[startIndex]!=-1:
        print("just return ", numOfWays[startIndex])
        return numOfWays[startIndex]
    else:
        count = 0
        # 这道题题目要求的是每一个prime的大小不超过1000，所以每个prime最多只能是3位数
        for i in range(startIndex,min(startIndex+3,len(s))):
            # i对应的是我们当前要检测是不是prime的这个数字的最后一位数在s里的index
            number = int(s[startIndex:i+1])
            print("startIndex: {index}, startDigit:{digit}, number under consideration is: {number} ".format(index=startIndex,
                                                                                                 digit=s[startIndex],
                                                                                                 number=number))
            if isPrime(number):
                # 如果i就是s的最后一位的话，那么s[i]后面没有数字了，这个branch的recursion不需要再向下
                # 进行了，直接给从count加1，这个加1对应的就是这一种分法
                # 比如当number是最后一个3时，i==len(s)-1,这时count上加的1对应的就是[11,3,7,3]这种分法
                if i == len(s)-1:
                    count+=1
                    print("startIndex: {index}, startDigit:{digit}, i was last index, count is:{count}".format(
                        index=startIndex,
                        digit=s[startIndex],
                        count=count))
                # 如果i不是s的最后一位，则对startIndex为i+1的substring继续invoke这个recursive function
                else:
                    count+=countNumOfWays(s,i+1,numOfWays)
                    print("startIndex: {index}, startDigit:{digit}, count is:{count}".format(
                        index=startIndex,
                        digit=s[startIndex],
                        count=count))
        numOfWays[startIndex] = count
        return count

print(countNumOfWays("11373",0,[-1,-1,-1,-1,-1]))




