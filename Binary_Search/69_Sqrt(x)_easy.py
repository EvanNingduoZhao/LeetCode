class Solution:
    def mySqrt(self, x: int) -> int:
        #base case 如果x=0或者1的话直接return x就好了
        if x==0 or x==1:
            return x
        else:
            #开始binary search
            start=1
            end=x
            while start<=end:
                #因为每次end都被assign成mid，而end被assign成mid的时候都是mid的平方大于x的时候
                #而我们要truncate所有的小数部分，即15应该return 3
                #既然end都是等于平方大于x的mid，那么end永远不可能是结果
                #所以在end就是start的下一个的时候，直接return start
                if end-start==1:
                    return start
                mid=(start+end)//2
                ms=mid*mid
                if ms==x:
                    return mid
                elif ms>x:
                    end=mid
                #当mid的平方小于x的时候start=mid
                #因为我们对于小数部分只有舍没有进，所以对于飞完全平方数而言，
                #return的结果肯定是一个平方小于自己的数，所以start是可能成为return的结果的
                else:
                    start=mid