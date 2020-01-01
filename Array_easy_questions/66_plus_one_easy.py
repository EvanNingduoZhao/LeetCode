# a much simpler version of 加法竖式 但注意如果input是[9,9,9,9]一类的话，要在进位运算的最后在输出list的最前面加一个1
# 这道题教我们如何简单地运用carry
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    length=len(digits)
    if digits[length-1]<9:
        digits[length-1]+=1
        return digits
    else:
        digits[length-1]=0
        carry=1
        pos=length-2
        for i in range(pos+1):
            sum=carry+digits[pos-i]
            if sum==10:
                digits[pos-i]=0
                carry=1
            else:
                digits[pos-i]=sum
                carry=0
                break
        if carry==1:#如果input是[9,9,9,9]一类的话，要在进位运算的最后在输出list的最前面加一个1
            digits.insert(0,1)
        return digits

input=[9,9,9,9,9]
print(plusOne(input))