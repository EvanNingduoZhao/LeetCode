def rotateNum(nums):
    outOfOrderCount = 0
    increase = False
    decrease = False
    for i in range(1,len(nums)):
        