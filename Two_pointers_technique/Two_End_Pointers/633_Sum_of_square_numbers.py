#这道题在本质上和167题是一样的，都是在sorted array中找有没有符合条件的一对数
import math
def judgeSquareSum(c):
    #当然题中的input不是一个sorted array，而是一个数
    #那我们自己制造这个sorted array，如果C是A和B的平方和
    #那A和B一定都是小于等于C的square root的
    #所以我们要进行search的sorted array其实就应该是从0到c的square root的这个连续的list
    i = 0
    j = int(math.sqrt(c))
    print(j)
    #其余的方法和167题一致
    while (i < j):
        print("i is "+str(i))
        print("j is " + str(j))
        print("c is " + str(c))
        print("j square is " + str(j ^ 2))
        if i*i + j*j < c:
            i += 1
        elif i*i + j*j > c:
            j -= 1
        else:
            return True
    return False

print(judgeSquareSum(5))