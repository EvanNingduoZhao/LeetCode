# pretty straight forward question doesn't need much of explanation
class Solution:
    def reverse(x: int) -> int:
        upper=2**31-1
        lower=2**31*(-1)
        negative=False
        if x<0:
            negative=True
            x=x*(-1)
        if x>-10 and x<10:
            return x
        l=[]
        s=''
        while x%10 != x:
            l.append(x%10)
            x=x//10
        l.append(x)
        for i in l:
            s+=str(i)
        ans=int(s)
        if negative==True and (-1)*int(s)>=lower:
            return (-1)*int(s)
        elif negative == False and int(s)<=upper:
            return int(s)
        else:
            return 0

    def reverse_shorter(x):
        s = (x > 0) - (x < 0)
        r = int(str(s * x)[::-1])
        return s * r * (r < 2 ** 31)

    print(reverse(123))
