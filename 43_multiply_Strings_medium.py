
def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    # len2=len(num2)
    # len1=len(num1)
    # multiply_carry=0
    # sum_carry=0
    # digit_position = len1+len2-1
    # ans=[0]*(len1+len2)
    # for i in range(len2):
    #     print('we are taking %s in num2'%num2[len2-1-i])
    #     for j in range(len1):
    #         product=int(num2[len2-1-i])*int(num1[len1-1-j])+multiply_carry
    #         print('%s times %s then plus a carry of %d is %d'%(num2[len2-1-i],num1[len1-1-j],multiply_carry,product))
    #         multiply_carry = product//10
    #         digit= product-10*multiply_carry
    #         sum=ans[digit_position]+digit+sum_carry
    #         if sum<10:
    #             ans[digit_position]=sum
    #             print('after if ans is ')
    #             print(ans)
    #             sum_carry=0
    #         else:
    #             mod=sum%10
    #             ans[digit_position]=mod
    #             print('after else ans is ')
    #             print(ans)
    #             sum_carry=sum//10
    #         digit_position=digit_position-1
    #     ans[digit_position]=ans[digit_position]+multiply_carry+sum_carry
    #     print('after special adding ans is ')
    #     print(ans)
    #     multiply_carry=0
    #     sum_carry=0
    #     digit_position+=len(num1)-1
    #
    # stringans = [str(i) for i in ans]
    # print('stringans is ')
    # print(stringans)
    #
    # result = "".join(stringans)
    # ifzero=True
    # for i in result:
    #     if i != '0':
    #         ifzero=False
    #         break
    # if ifzero==True:
    #     return '0'
    # else:
    #     for i in range(len(stringans)):
    #         if stringans[i]!='0':
    #             start=i
    #             break
    #
    #     return "".join( stringans[start:])


    # 上面我的方法是乘的时候算一次carry，加的时候再算一次carry，而下面的答案是直接把乘的结果加到要list对应的一位，这样乘和加的carry可以一步完成
    product = [0] * (len(num1) + len(num2))
    pos = len(product) - 1

    for n1 in reversed(num1):
        tempPos = pos
        for n2 in reversed(num2):
            product[tempPos] += int(n1) * int(n2)
            product[tempPos - 1] += product[tempPos] // 10
            product[tempPos] %= 10
            tempPos -= 1
        pos -= 1
    print(product)
    pt = 0
    while pt < len(product) - 1 and product[pt] == 0:
        pt += 1

    return ''.join(map(str, product[pt:]))

print(multiply('723','456'))


