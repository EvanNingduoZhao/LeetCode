import math
def judgeSquareSum(c):
    i = 0
    j = int(math.sqrt(c))
    print(j)
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